#!/usr/bin/env python3
"""Prepare a local source lock, or verify a published lock. Never commits or pushes."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.agents/skills/static-graphic-design-creator/scripts'))
import skill_lifecycle as life

MANIFEST = 'config/chatgpt-skill-sources.json'
BOOTSTRAP = 'config/chatgpt-skills.json'
HISTORY = 'config/release-history.json'
API = 'https://api.github.com/repos/FrameCoreWorks/static-graphic-design-creator'
RAW = 'https://raw.githubusercontent.com/FrameCoreWorks/static-graphic-design-creator/'


def git(*args, root=ROOT):
    return subprocess.check_output(['git', '-C', str(root), *args])


def source_files(source, root=ROOT):
    life.require(re.fullmatch(r'[0-9a-f]{40}', source), 'An exact source commit is required')
    life.require(git('cat-file', '-t', source, root=root).strip() == b'commit', 'Source is not a commit')
    files = {}
    for row in git('ls-tree', '-rz', source, '--', life.SOURCE_ROOT, root=root).split(b'\0'):
        if not row:
            continue
        header, path_bytes = row.split(b'\t', 1)
        mode, kind, _ = header.split()
        life.require(mode in {b'100644', b'100755'} and kind == b'blob', 'Non-regular source entry')
        path = path_bytes.decode('utf-8')
        relative = path.removeprefix(life.SOURCE_ROOT + '/')
        life.safe_path(relative)
        life.require(not relative.startswith('local/'), 'Personal extensions cannot enter a source release')
        files[relative] = git('show', source + ':' + path, root=root)
    life.require(files, 'Empty source tree')
    return files


def pending_report(release_id, source, evaluation):
    cases = re.findall(r'^(\d+\. [^:\n]+):', evaluation, re.M)
    life.require(cases and len(cases) == len(set(cases)), 'Invalid host case inventory')
    text = f'''# Host Evaluation Record: {release_id}

| Field | Value |
| --- | --- |
| Release ID | `{release_id}` |
| Immutable source commit | `{source}` |
| Record status | `pending_host_evaluation` |
| ChatGPT Work account/workspace eligibility | `Unknown` |
| Codex account/environment eligibility | `Unknown` |
| Evaluated on | `Unknown` |

Prepared locally. Publication, native installation and live host behavior have not
been verified by this generated record. A source change invalidates prior host
evidence for this candidate; deterministic checks are recorded separately.

| Case | ChatGPT Work | Codex | Evidence / deviation |
| --- | --- | --- | --- |
'''
    return text + ''.join('| ' + case + ' | pending | pending | Unknown |\n' for case in cases)


def validate_history(history, root=ROOT):
    life.require(history['repository'] == life.REPOSITORY, 'Wrong history repository')
    seen = set()
    for entry in history['releases']:
        life.require(entry['release_id'] not in seen, 'Duplicate historical release')
        seen.add(entry['release_id'])
        commit = entry['manifest_commit']
        life.require(re.fullmatch(r'[0-9a-f]{40}', commit), 'Historical manifest commit must be immutable')
        data = git('show', commit + ':' + MANIFEST, root=root)
        life.require(life.sha(data) == entry['manifest_sha256'], 'Historical manifest digest mismatch')
        m = life.parse_json(data)
        life.validate_manifest(m, entry['release_id'])
        life.require(m['ref'] == entry['immutable_source_commit'], 'Historical source mismatch')
        life.verify_bundle(source_files(m['ref'], root), m)
    return len(seen)


def prepare_lock(source, root=ROOT):
    """Derive both configs from committed bytes, refusing a mixed working bundle."""
    files = source_files(source, root)
    life.verify_result(files, life.read_tree(root / life.SOURCE_ROOT))
    record = life.parse_json(files[life.RECORD])
    life.require(record['repository'] == life.REPOSITORY and record['skill_name'] == life.NAME, 'Wrong source identity')
    life.require(record['release_id'] == 'v' + record['version'], 'Source version mismatch')
    release_id = record['release_id']
    # Published refs must be fetched before preparation. Never silently reuse one.
    for prefix in ('refs/tags/', 'refs/remotes/origin/'):
        result = subprocess.run(['git', '-C', str(root), 'show-ref', '--verify', '--quiet', prefix + release_id])
        life.require(result.returncode == 1, 'Release ref already exists or cannot be checked: ' + release_id)
    manifest = life.parse_json((root / MANIFEST).read_bytes())
    config = life.parse_json((root / BOOTSTRAP).read_bytes())
    manifest.update(version=record['version'], release_id=release_id, release_channel=record['release_channel'],
                    immutable_source_commit=source, ref=source)
    manifest['skills'][0]['files'] = [
        {'path': path, 'repository_path': life.SOURCE_ROOT + '/' + path,
         'raw_url': RAW + source + '/' + life.SOURCE_ROOT + '/' + path, 'sha256': life.sha(data)}
        for path, data in sorted(files.items())]
    config['version'] = record['version']
    config['release'].update(id=release_id, channel=record['release_channel'], immutable_source_commit=source)
    life.validate_bootstrap(config, manifest)
    life.verify_bundle(files, manifest)
    report_path = 'reports/host-evaluations/' + release_id + '.md'
    if (root / report_path).exists():
        existing = (root / report_path).read_text()
        observed = re.search(r'^\| \d+\. [^|]+ \| (?!pending \| pending \|)[^\n]+', existing, re.M)
        life.require(not observed, 'Existing host evidence must be preserved under its original release')
    updates = {
        MANIFEST: (json.dumps(manifest, indent=2, ensure_ascii=False) + '\n').encode(),
        BOOTSTRAP: (json.dumps(config, indent=2, ensure_ascii=False) + '\n').encode(),
        report_path: pending_report(release_id, source, (root / 'EVALUATION.md').read_text()).encode(),
    }
    history_path = root / HISTORY
    if history_path.exists():
        history = life.parse_json(history_path.read_bytes())
        validate_history(history, root)
        remote = subprocess.run(['git', '-C', str(root), 'rev-parse', '--verify', 'refs/remotes/origin/main'], capture_output=True, text=True)
        life.require(remote.returncode == 0, 'Fetch origin/main before preparing the release history')
        previous_lock = remote.stdout.strip()
        previous_bytes = git('show', previous_lock + ':' + MANIFEST, root=root)
        previous = life.parse_json(previous_bytes)
        life.verify_bundle(source_files(previous['ref'], root), previous)
        life.require(previous['release_id'] != release_id, 'This version is already public on the fetched main')
        existing = next((e for e in history['releases'] if e['release_id'] == previous['release_id']), None)
        if existing:
            life.require(existing['immutable_source_commit'] == previous['ref'], 'Previously published version changed source')
        else:
            history['releases'].append({'release_id': previous['release_id'], 'manifest_commit': previous_lock,
                                       'manifest_sha256': life.sha(previous_bytes), 'immutable_source_commit': previous['ref']})
        updates[HISTORY] = (json.dumps(history, indent=2) + '\n').encode()
    originals = {p: (root / p).read_bytes() if (root / p).exists() else None for p in updates}
    try:
        for path, data in updates.items():
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_bytes(data)
    except OSError:
        for path, data in originals.items():
            if data is None:
                (root / path).unlink(missing_ok=True)
            else:
                (root / path).write_bytes(data)
        raise
    return {'status': 'prepared_locally', 'release_id': release_id, 'source_commit': source,
            'files': len(files), 'written': list(updates)}


def fetch(url):
    request = Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'static-graphic-design-creator-release-check'})
    with urlopen(request, timeout=30) as response:
        return response.read()


def verify_public(lock, release_ref, fetcher=fetch):
    life.require(re.fullmatch(r'[0-9a-f]{40}', lock), 'Exact public lock commit required')
    life.require(re.fullmatch(r'v[0-9A-Za-z.\-]+', release_ref), 'Invalid release ref')
    config = life.parse_json(fetcher(RAW + lock + '/' + BOOTSTRAP))
    manifest = life.parse_json(fetcher(RAW + lock + '/' + MANIFEST))
    life.validate_bootstrap(config, manifest)
    life.require(manifest['release_id'] == release_ref, 'Public release ref identity mismatch')
    # Compare immutable manifest bytes through the version ref, not just its name.
    ref_config = life.parse_json(fetcher(RAW + release_ref + '/' + BOOTSTRAP))
    ref_manifest = life.parse_json(fetcher(RAW + release_ref + '/' + MANIFEST))
    life.require(ref_config == config and ref_manifest == manifest, 'Release ref contains another lock')
    main = life.parse_json(fetcher(API + '/commits/main'))['sha']
    version_head = life.parse_json(fetcher(API + '/commits/' + release_ref))['sha']
    life.require(main == lock and version_head == lock, 'Discovery/version ref does not point at the expected lock')
    source = manifest['immutable_source_commit']
    relation = life.parse_json(fetcher(API + '/compare/' + source + '...' + lock))
    life.require(relation['status'] in {'ahead', 'identical'}, 'Public source is not an ancestor of the lock')
    tree = life.parse_json(fetcher(API + '/git/trees/' + source + '?recursive=1'))
    life.require(tree.get('truncated') is False, 'Public tree inventory is incomplete')
    entries = [e for e in tree['tree'] if e['path'].startswith(life.SOURCE_ROOT + '/') and e['type'] != 'tree']
    life.require(all(e['type'] == 'blob' and e['mode'] in {'100644', '100755'} for e in entries), 'Unsafe public source entry')
    life.require({e['path'].removeprefix(life.SOURCE_ROOT + '/') for e in entries}
                 == {e['path'] for e in manifest['skills'][0]['files']}, 'Undeclared or missing public source file')
    with ThreadPoolExecutor(max_workers=4) as pool:
        bodies = list(pool.map(lambda e: (e['path'], fetcher(e['raw_url'])), manifest['skills'][0]['files']))
    life.verify_bundle(dict(bodies), manifest)
    runs = life.parse_json(fetcher(API + '/actions/workflows/validate.yml/runs?head_sha=' + lock + '&event=push&per_page=20'))
    candidates = [r for r in runs['workflow_runs'] if r['head_sha'] == lock and r['event'] == 'push'
                  and r['head_branch'] == 'main']
    life.require(candidates, 'Validation CI has not run for this public lock')
    latest = max(candidates, key=lambda r: r['id'])
    life.require(latest['status'] == 'completed' and latest['conclusion'] == 'success', 'Latest validation CI is pending or failed')
    life.require(life.parse_json(fetcher(API + '/commits/main'))['sha'] == lock
                 and life.parse_json(fetcher(API + '/commits/' + release_ref))['sha'] == lock, 'Public refs changed during verification')
    return {'status': 'public_release_verified', 'lock': lock, 'source': source, 'files': len(bodies),
            'manifest_sha256': life.sha(fetcher(RAW + lock + '/' + MANIFEST)), 'ci_run': latest['id']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    lock = sub.add_parser('lock', help='Write local configs and reset unexecuted candidate report')
    lock.add_argument('--source', required=True)
    public = sub.add_parser('verify-public', help='Read public refs, all source files and exact-head CI')
    public.add_argument('--lock', required=True)
    public.add_argument('--release-ref', required=True)
    args = parser.parse_args()
    try:
        result = prepare_lock(args.source) if args.command == 'lock' else verify_public(args.lock, args.release_ref)
        print(json.dumps(result, indent=2))
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({'status': 'blocked_release_verification', 'error': str(exc)}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
