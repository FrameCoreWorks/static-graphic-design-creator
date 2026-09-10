#!/usr/bin/env python3
"""Repository integrity tests; never evidence of model or visual performance.
--working-tree checks the previous pinned baseline and edited draft structure.
Only default mode verifies that the current source bundle matches its release.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = '.agents/skills/static-graphic-design-creator'
SKILL = ROOT / SOURCE_ROOT
NAME = 'static-graphic-design-creator'
REPOSITORY = 'https://github.com/FrameCoreWorks/' + NAME
sys.path.insert(0, str(SKILL / 'scripts'))
from skill_lifecycle import validate_manifest, validate_bootstrap, classify_delta
sys.path.insert(0, str(ROOT / 'scripts'))
from release import validate_history

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key}')
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def read_json(path):
    def unique(pairs):
        result = {}
        for k, v in pairs:
            if k in result:
                raise ValueError(f'Duplicate JSON key: {k}')
            result[k] = v
        return result
    return json.loads(Path(path).read_text(), object_pairs_hook=unique)

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', f'{commit}:{path}'], cwd=ROOT)

def validate_host_report(text, release_id, commit, expected_cases=None, stable=False):
    fields = dict(re.findall(r'^\| ([^|]+?) \| `([^`]+)` \|$', text, re.M))
    require(fields.get('Release ID') == release_id, 'Host report release mismatch')
    require(fields.get('Immutable source commit') == commit, 'Host report source mismatch')
    rows = re.findall(r'^\| (\d+)\. ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', text, re.M)
    require(rows and len({r[0] for r in rows}) == len(rows), 'Missing/duplicate host cases')
    if expected_cases is not None:
        require({r[0] for r in rows} == set(expected_cases), 'Host report case inventory mismatch')
    for _, name, work, codex, evidence in rows:
        require(work.strip() in {'pending', 'pass', 'fail', 'blocked', 'not_applicable'} and
                codex.strip() in {'pending', 'pass', 'fail', 'blocked', 'not_applicable'}, f'Invalid host status: {name}')
        if work.strip() != 'pending' or codex.strip() != 'pending':
            require(evidence.strip() not in {'', 'Unknown', 'pending'}, f'Missing evidence: {name}')
    status = fields.get('Record status')
    require(status in {'pending_host_evaluation', 'partial_host_evaluation', 'completed_host_evaluation'}, 'Invalid report status')
    if status == 'completed_host_evaluation':
        require(all(r[2].strip() != 'pending' and r[3].strip() != 'pending' for r in rows), 'Completed report contains pending cases')
    if stable:
        require(status == 'completed_host_evaluation', 'Stable release needs completed host evaluation')
        require(all(r[2].strip() in {'pass', 'not_applicable'} and r[3].strip() in {'pass', 'not_applicable'} for r in rows), 'Stable release contains unresolved or failed host cases')
        for key in ('Evaluated on', 'ChatGPT Work account/workspace eligibility', 'Codex account/environment eligibility'):
            require(fields.get(key) not in {None, '', 'Unknown'}, 'Stable evaluation metadata unresolved: ' + key)
    return rows

def check_documents():
    docs = list(SKILL.rglob('*.md')) + [ROOT / n for n in ('README.md', 'CHATGPT_INSTALL.md', 'CHATGPT_UPDATE.md', 'CODEX_INSTALL.md', 'CODEX_UPDATE.md')]
    for path in docs:
        content = path.read_text()
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            if '://' in link or link.startswith('#'):
                continue
            dest = (path.parent / link.split('#')[0]).resolve()
            require(dest.is_relative_to(ROOT) and dest.exists(), f'Broken or escaping link: {path}: {link}')
        for block in re.findall(r'```yaml\n(.*?)```', content, re.S):
            yaml.load(block, Loader=UniqueLoader)
        require(not any(p in content for p in ['/root/.codex', '/workspace/scratch', '[TODO:']), f'Private path or scaffold: {path}')
    frontmatter = yaml.load((SKILL / 'SKILL.md').read_text().split('---', 2)[1], Loader=UniqueLoader)
    require(frontmatter['name'] == NAME and frontmatter['description'].strip(), 'Invalid frontmatter')
    ui = yaml.load((SKILL / 'agents/openai.yaml').read_text(), Loader=UniqueLoader)
    require(ui['interface']['display_name'], 'Missing display name')
    require(ui['policy']['allow_implicit_invocation'] is False, 'Explicit activation policy drift')
    for k in ('icon_small', 'icon_large'):
        if k in ui['interface']:
            require((SKILL / ui['interface'][k]).is_file(), 'Missing declared icon')
    for p in ROOT.glob('tests/fixtures/*.json'):
        fixture = read_json(p)
        ids = [c['id'] for c in fixture['cases']]
        require(ids and len(ids) == len(set(ids)), f'Empty or duplicate fixture IDs: {p}')
        if fixture.get('evaluation_kind') == 'manual_forward_test':
            for case in fixture['cases']:
                require(case.get('prompt', '').strip() and case.get('expected_observables') and 'must_not' in case, f'Incomplete manual case: {p}: {case["id"]}')

def check_negative_cases(manifest):
    mutations = [lambda m: m.update(ref='main'), lambda m: m.update(release_id='v999.0.0'),
        lambda m: m['skills'][0]['files'][0].update(path='../escape'),
        lambda m: m['skills'][0]['files'].append(copy.deepcopy(m['skills'][0]['files'][0])),
        lambda m: m['skills'][0]['files'][0].update(raw_url='https://example.com/file')]
    for mutate in mutations:
        bad = copy.deepcopy(manifest)
        mutate(bad)
        try:
            validate_manifest(bad)
        except (AssertionError, ValueError):
            pass
        else:
            raise AssertionError('Malformed manifest accepted')
    try:
        validate_manifest(manifest, 'v999.0.0')
    except (AssertionError, ValueError):
        pass
    else:
        raise AssertionError('Wrong baseline release accepted')
    for snippet in ('task_mode: generate\ntask_mode:\n', 'outer:\n  x: 1\n  x: 2\n'):
        try:
            yaml.load(snippet, Loader=UniqueLoader)
        except ValueError:
            pass
        else:
            raise AssertionError('Duplicate YAML key accepted')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--working-tree', action='store_true')
    args = parser.parse_args()
    m = read_json(ROOT / 'config/chatgpt-skill-sources.json')
    config = read_json(ROOT / 'config/chatgpt-skills.json')
    paths = validate_manifest(m)
    commit = m['immutable_source_commit']
    validate_bootstrap(config, m)
    validate_history(read_json(ROOT / 'config/release-history.json'))
    ancestor = subprocess.run(['git', 'merge-base', '--is-ancestor', commit, 'HEAD'], cwd=ROOT)
    require(ancestor.returncode == 0, 'Pinned source is not an ancestor of this checkout')
    tree = subprocess.check_output(['git', 'ls-tree', '-r', commit, SOURCE_ROOT], cwd=ROOT).decode()
    pinned_paths = set()
    for line in tree.splitlines():
        header, path = line.split('\t', 1)
        mode, kind, _ = header.split()
        require(mode in {'100644', '100755'} and kind == 'blob', 'Non-regular pinned source: ' + path)
        pinned_paths.add(path.removeprefix(SOURCE_ROOT + '/'))
    require(pinned_paths == paths, 'Pinned inventory mismatch')
    for e in m['skills'][0]['files']:
        require(sha(git_bytes(commit, e['repository_path'])) == e['sha256'], f'Pinned hash mismatch: {e["path"]}')
        if not args.working_tree:
            p = SKILL / e['path']
            require(p.is_file() and not p.is_symlink() and sha(p.read_bytes()) == e['sha256'], f'Working source differs from lock: {e["path"]}')
    record = json.loads(git_bytes(commit, SOURCE_ROOT + '/references/source-release.json'))
    require(record['repository'] == REPOSITORY and record['skill_name'] == NAME, 'Pinned identity mismatch')
    require(record['version'] == m['version'] and record['release_id'] == m['release_id'], 'Pinned release mismatch')
    require(record['release_channel'] == m['release_channel'] == config['release']['channel'], 'Release channel mismatch')
    if not args.working_tree:
        require({str(p.relative_to(SKILL)) for p in SKILL.rglob('*') if p.is_file()} == paths, 'Working bundle inventory mismatch')
    check_documents()
    from layer_assets import validate_plan
    validate_plan(read_json(SKILL / "templates/layer-plan.json"))
    check_negative_cases(m)
    report = (ROOT / 'reports/host-evaluations' / (m['release_id'] + '.md')).read_text()
    expected_cases = re.findall(r'^(\d+)\. [^:\n]+:', (ROOT / 'EVALUATION.md').read_text(), re.M)
    require(len(expected_cases) == len(set(expected_cases)), 'Duplicate required evaluation cases')
    rows = validate_host_report(report, m['release_id'], commit, None if args.working_tree else expected_cases, m['release_channel'] == 'stable')
    validate_host_report(report.replace('| pending | pending | Unknown |', '| pass | pending | observed test output |', 1), m['release_id'], commit)
    # Candidate pending results are valid records, but never a stable-release pass.
    pending = re.sub(r'\| (\d+\. [^|]+) \| [^|]+ \| [^|]+ \| [^|]+ \|', r'| \1 | pending | pending | Unknown |', report)
    pending = re.sub(r'\| Record status \| `[^`]+` \|', '| Record status | `pending_host_evaluation` |', pending)
    try:
        validate_host_report(pending, m['release_id'], commit, stable=True)
    except AssertionError:
        pass
    else:
        raise AssertionError('Pending candidate accepted as stable')
    try:
        validate_host_report(report, m['release_id'], commit, {'missing-case'})
    except AssertionError:
        pass
    else:
        raise AssertionError('Missing host case accepted')
    cases = read_json(ROOT / 'tests/fixtures/update-eval-cases.json')['cases']
    for c in cases:
        require(classify_delta(c['base'], c['target'], c['installed']) == c['expected'], f'Delta failed: {c["id"]}')
    print(f'Package checks passed; {len(paths)} pinned files; {len(cases)} three-way delta cases; {len(rows)} host cases recorded (not executed). ' + ('WORKING DRAFT, not release certification.' if args.working_tree else 'Release lock verified locally.'))

if __name__ == '__main__':
    main()
