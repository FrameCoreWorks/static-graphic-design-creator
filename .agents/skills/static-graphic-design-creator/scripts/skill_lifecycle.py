#!/usr/bin/env python3
"""Verify source bundles and plan an existing-Skill update. Never writes or saves."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

NAME = 'static-graphic-design-creator'
REPOSITORY = 'https://github.com/FrameCoreWorks/' + NAME
SOURCE_ROOT = '.agents/skills/' + NAME
RECORD = 'references/source-release.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(value):
    p = PurePosixPath(value)
    require(str(p) == value and not p.is_absolute() and '..' not in p.parts
            and value not in {'', '.'} and '\\' not in value, 'Unsafe bundle path: ' + value)
    return p


def validate_manifest(m, expected_release=None):
    require(m['repository'] == REPOSITORY, 'Wrong repository')
    require(m['release_id'] == 'v' + m['version'], 'Release/version mismatch')
    if expected_release is not None:
        require(m['release_id'] == expected_release, 'Wrong baseline release')
    commit = m['immutable_source_commit']
    require(re.fullmatch(r'[0-9a-f]{40}', commit), 'Immutable commit required')
    require(m['ref'] == commit and m['release_ref_type'] == 'immutable_git_commit', 'Source ref mismatch')
    require(len(m['skills']) == 1, 'Exactly one Skill required')
    skill = m['skills'][0]
    require(skill['name'] == NAME and skill['source_root'] == SOURCE_ROOT, 'Wrong source identity')
    paths = set()
    for entry in skill['files']:
        path = entry['path']
        safe_path(path)
        require(not path.startswith('local/'), 'The local namespace cannot be published as source')
        require(path not in paths, 'Duplicate manifest path')
        paths.add(path)
        require(entry['repository_path'] == SOURCE_ROOT + '/' + path, 'Wrong repository mapping')
        require(entry['raw_url'] == 'https://raw.githubusercontent.com/FrameCoreWorks/' + NAME
                + '/' + commit + '/' + SOURCE_ROOT + '/' + path, 'Wrong immutable URL')
        require(re.fullmatch(r'[0-9a-f]{64}', entry['sha256']), 'Invalid SHA-256')
    require({'SKILL.md', RECORD} <= paths, 'Missing identity files')
    return paths


def validate_bootstrap(config, manifest):
    validate_manifest(manifest)
    require(config['repository'] == manifest['repository'], 'Bootstrap repository mismatch')
    require(config['version'] == manifest['version'], 'Bootstrap version mismatch')
    release = config['release']
    require(release['id'] == manifest['release_id'] and release['channel'] == manifest['release_channel'],
            'Bootstrap release/channel mismatch')
    require(release['immutable_source_commit'] == manifest['immutable_source_commit']
            and release['source_ref_type'] == 'immutable_git_commit', 'Bootstrap source mismatch')
    require(release['bootstrap_ref'] == manifest['release_bootstrap_ref']
            and release['bootstrap_ref_type'] == manifest['release_bootstrap_ref_type'],
            'Bootstrap discovery mismatch')
    require(config['bootstrap']['source_manifest_path'] == 'config/chatgpt-skill-sources.json',
            'Wrong source manifest location')
    require(len(config['skills']) == 1 and config['skills'][0]['name'] == NAME
            and config['skills'][0]['source_root'] == SOURCE_ROOT, 'Bootstrap Skill identity mismatch')
    require('files' not in config['skills'][0], 'Per-file inventory belongs only in the source manifest')


def read_tree(root):
    root = Path(root)
    require(root.is_dir() and not root.is_symlink(), 'Bundle directory unavailable or symlinked')
    files = {}
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink(), 'Symlink in bundle: ' + str(path.relative_to(root)))
        if path.is_dir():
            continue
        require(path.is_file(), 'Non-regular bundle entry')
        name = path.relative_to(root).as_posix()
        safe_path(name)
        files[name] = path.read_bytes()
    return files


def digests(files):
    return {path: sha(data) for path, data in files.items()}


def verify_bundle(files, manifest):
    paths = validate_manifest(manifest)
    require(set(files) == paths, 'Source inventory mismatch')
    for entry in manifest['skills'][0]['files']:
        require(sha(files[entry['path']]) == entry['sha256'], 'Source hash mismatch: ' + entry['path'])
    record = parse_json(files[RECORD])
    require(record['repository'] == REPOSITORY and record['skill_name'] == NAME, 'Wrong source record identity')
    require(record['release_id'] == manifest['release_id'] and record['version'] == manifest['version']
            and record['release_channel'] == manifest['release_channel'], 'Source record release mismatch')


def classify_delta(base, target, installed):
    """Digest comparison; unchanged local changes are retained, not auto-overwritten."""
    b, t, i = set(base), set(target), set(installed)
    changed = {p for p in b & t if base[p] != target[p]}
    added, removed = t - b, b - t
    modified = {p for p in b & i if base[p] != installed[p]}
    deleted, local_added = b - i, i - b
    conflicts = {p for p in (modified | deleted) & (changed | removed)
                 if installed.get(p) != target.get(p)}
    conflicts |= {p for p in added & local_added if installed[p] != target[p]}
    return {k: sorted(v) for k, v in {
        'changed': changed, 'new': added, 'removed': removed, 'unchanged': (b & t) - changed,
        'local_modified': modified, 'local_deleted': deleted, 'local_added': local_added,
        'conflicts': conflicts,
        'apply': {p for p in changed | added | removed if installed.get(p) != target.get(p)} - conflicts,
    }.items()}


def compare(base, target, installed):
    """Produce a read-only proposal, including all conflicting content differences."""
    for files in (base, target, installed):
        for path in files:
            safe_path(path)
    require(RECORD in base and RECORD in target and RECORD in installed, 'Baseline record unavailable')
    baseline_record, target_record, installed_record = [parse_json(f[RECORD]) for f in (base, target, installed)]
    for record in (baseline_record, target_record, installed_record):
        require(record['repository'] == REPOSITORY and record['skill_name'] == NAME, 'Source identity mismatch')
        require(record['release_id'] == 'v' + record['version'], 'Record version mismatch')
    require(installed_record['release_id'] == baseline_record['release_id'], 'Installed baseline does not match')
    delta = classify_delta(digests(base), digests(target), digests(installed))
    matches = sorted(p for p in target if installed.get(p) == target[p])
    deviations = sorted(p for p in set(target) | set(installed) if installed.get(p) != target.get(p))
    status = ('blocked_local_conflict' if delta['conflicts'] else
              'ready_for_review' if delta['apply'] else
              'local_customizations_preserved' if deviations else 'already_up_to_date')
    previews = {}
    for path in delta['conflicts']:
        content = {'base': base.get(path), 'installed': installed.get(path), 'target': target.get(path)}
        try:
            texts = {k: (v or b'').decode('utf-8').splitlines(keepends=True) for k, v in content.items()}
            previews[path] = {
                'kind': 'add_add' if path not in base else 'three_way',
                'base_to_installed': ''.join(difflib.unified_diff(texts['base'], texts['installed'], fromfile='base/' + path, tofile='installed/' + path)),
                'installed_to_target': ''.join(difflib.unified_diff(texts['installed'], texts['target'], fromfile='installed/' + path, tofile='target/' + path)),
                'resolution': 'review_required',
            }
        except UnicodeDecodeError:
            previews[path] = {'kind': 'binary', 'sha256': {k: sha(v) if v is not None else None for k, v in content.items()}, 'resolution': 'review_required'}
    return {'status': status, 'installed_base': installed_record['release_id'], 'target_release': target_record['release_id'],
            'delta': delta, 'already_target': matches, 'target_deviations': deviations,
            'installed_snapshot': digests(installed), 'conflict_previews': previews,
            'apply_mode': 'selective_file_update' if status == 'ready_for_review' else 'none',
            'approval_required_before_save': status in {'ready_for_review', 'blocked_local_conflict'}}


def build_proposal(base, target, installed, resolutions=None):
    """Build expected bytes in memory only; caller must obtain approval before a host save.

    Resolve every conflict with 'target', 'local', bytes for a reviewed merge, or None
    for a reviewed deletion. This function never chooses a resolution on the user's behalf.
    """
    plan = compare(base, target, installed)
    resolutions = resolutions or {}
    require(set(resolutions) == set(plan['delta']['conflicts']), 'Resolve all conflicts, and only conflicts')
    result = dict(installed)
    for path in plan['delta']['apply']:
        if path in target:
            result[path] = target[path]
        else:
            result.pop(path, None)
    for path, choice in resolutions.items():
        value = target.get(path) if choice == 'target' else installed.get(path) if choice == 'local' else choice
        require(value is None or isinstance(value, bytes), 'Invalid resolved content: ' + path)
        if value is None:
            result.pop(path, None)
        else:
            result[path] = value
    require(result.get(RECORD) == target[RECORD], 'Proposed source record must equal the target base')
    return result


def verify_result(expected, actual):
    """Use before save for input-drift detection, and after save for exact readback."""
    missing, extra = set(expected) - set(actual), set(actual) - set(expected)
    changed = {p for p in set(expected) & set(actual) if expected[p] != actual[p]}
    require(not (missing or extra or changed), 'Snapshot/readback mismatch: ' + json.dumps(
        {'missing': sorted(missing), 'extra': sorted(extra), 'changed': sorted(changed)}))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True, type=Path, help='Verified prior source directory')
    parser.add_argument('--target', required=True, type=Path, help='Verified target source directory')
    parser.add_argument('--installed', required=True, type=Path, help='Existing Skill directory; read only')
    parser.add_argument('--baseline-manifest', required=True, type=Path)
    parser.add_argument('--target-manifest', required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        base, target, installed = [read_tree(p) for p in (args.baseline, args.target, args.installed)]
        verify_bundle(base, parse_json(args.baseline_manifest.read_bytes()))
        verify_bundle(target, parse_json(args.target_manifest.read_bytes()))
        plan = compare(base, target, installed)
        plan['hash_verification'] = 'verified'
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 1 if plan['status'] == 'blocked_local_conflict' else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'blocked_verification', 'error': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
