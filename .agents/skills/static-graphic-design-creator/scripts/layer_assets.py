#!/usr/bin/env python3
"""Read-only layer registry and delivery checks. Never renders, saves or grants approval."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile


SIDECARS = {'layer-plan.json', 'ASSEMBLY.md', 'ASSET_INDEX.json'}
DIGEST = re.compile(r'[0-9a-f]{64}')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def decode(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON key: ' + key)
            result[key] = value
        return result
    def invalid(value):
        raise ValueError('Non-finite JSON number: ' + value)
    return json.loads(data, object_pairs_hook=unique, parse_constant=invalid)


def load(path):
    return decode(Path(path).read_bytes())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def known_text(value):
    return isinstance(value, str) and bool(value.strip()) and value.strip() != 'Unknown'


def safe_path(value):
    require(isinstance(value, str) and value and '\\' not in value and ':' not in value
            and not any(ord(c) < 32 for c in value), 'Unsafe file path')
    path = PurePosixPath(value)
    require(not path.is_absolute() and '..' not in path.parts and str(path) == value
            and value != '.', 'Unsafe relative file path: ' + value)
    return path


def local_file(root, name):
    relative = safe_path(name)
    root = Path(root).resolve()
    path = root
    for part in relative.parts:
        path = path / part
        require(not path.is_symlink(), 'Symlink is not a delivery file: ' + name)
    require(path.is_file() and path.resolve().is_relative_to(root), 'Missing or escaping file: ' + name)
    return path


def number(value, positive=False):
    return type(value) in {int, float} and math.isfinite(value) and (not positive or value > 0)


def validate_plan(plan):
    require(plan['schema_version'] == 1 and type(plan['schema_version']) is int, 'Unsupported layer plan version')
    require(known_text(plan['project_id']) and type(plan['revision']) is int and plan['revision'] > 0, 'Invalid project identity/revision')
    require(plan['mode'] in {'from_scratch', 'from_flattened'}, 'Invalid creation mode')
    canvas = plan['canvas']
    for key in ('width', 'height'):
        require(canvas[key] == 'Unknown' or type(canvas[key]) is int and canvas[key] > 0, 'Invalid canvas dimensions')
    composition = plan['composition']
    for key in ('objective', 'lighting', 'perspective'):
        require(isinstance(composition[key], str), 'Invalid composition field: ' + key)
    lock = composition['concept_lock']
    require(isinstance(lock, (str, dict)), 'Invalid concept lock')
    if isinstance(lock, dict):
        for key in ('premise', 'mechanism', 'distinctive_hook'):
            require(known_text(lock[key]), 'Incomplete structured concept lock')
        for key in ('allowed_adaptations', 'forbidden_substitutions'):
            require(isinstance(lock[key], list) and all(isinstance(v, str) for v in lock[key]), 'Invalid concept permissions')
    for key in ('palette', 'reserved_zones'):
        require(isinstance(composition[key], list) and all(isinstance(v, str) for v in composition[key]), 'Invalid ' + key)
    copy_ids = set()
    for item in composition['copy']:
        require(known_text(item['id']) and item['id'] not in copy_ids, 'Duplicate or invalid copy ID')
        copy_ids.add(item['id'])
        require(isinstance(item['text'], str) and item['status'] in {'draft', 'locked'}, 'Invalid project copy')
        require(isinstance(item['source'], str), 'Missing copy provenance')
    assets = plan['assets']
    require(isinstance(assets, list) and assets, 'Empty asset inventory')
    by_id, paths, z_indices, allocated, pending = {}, set(), set(), set(), []
    for asset in assets:
        aid = asset['id']
        require(known_text(aid) and aid not in by_id, 'Duplicate or invalid asset ID')
        by_id[aid] = asset
        require(asset['route'] in {'raster', 'editable_text'}, 'Unsupported asset route')
        require(known_text(asset['role']) and isinstance(asset['treatment'], str), 'Missing asset role/treatment')
        z = asset['z_index']
        require(type(z) is int and z not in z_indices, 'Ambiguous layer stacking')
        z_indices.add(z)
        require(number(asset['opacity']) and 0 <= asset['opacity'] <= 1, 'Invalid opacity')
        require(known_text(asset['blend_mode']) and asset['blend_support'] in {'verified', 'unsupported', 'Unknown'}, 'Invalid blend intent/support')
        require(asset['transparency'] in {'opaque', 'alpha', 'not_applicable', 'Unknown'}, 'Invalid transparency requirement')
        geometry = asset['geometry']
        require(geometry['canvas_mode'] in {'full_canvas', 'cropped'}, 'Invalid canvas mode')
        for key in ('x', 'y', 'width', 'height', 'rotation'):
            require(geometry[key] == 'Unknown' or number(geometry[key], key in {'width', 'height'}), 'Invalid placement: ' + key)
        if geometry['canvas_mode'] == 'full_canvas':
            require((geometry['x'], geometry['y'], geometry['rotation']) == (0, 0, 0), 'Full canvas must have origin placement and no rotation')
            require(geometry['width'] == canvas['width'] and geometry['height'] == canvas['height'], 'Full-canvas dimensions disagree')
        assigned = asset['copy_ids']
        require(isinstance(assigned, list) and len(assigned) == len(set(assigned)) and set(assigned) <= copy_ids, 'Invalid asset copy mapping')
        allocated.update(assigned)
        deps = asset['depends_on']
        require(isinstance(deps, list) and all(isinstance(d, str) for d in deps)
                and len(deps) == len(set(deps)) and aid not in deps, 'Invalid dependencies')
        require(isinstance(asset['dependency_note'], str) and (not deps or known_text(asset['dependency_note'])), 'Missing dependency explanation')
        require(isinstance(asset['coupled_elements'], list), 'Invalid coupled elements')
        versions = {}
        for version in asset['versions']:
            vid = version['id']
            require(known_text(vid) and vid not in versions, 'Duplicate version ID')
            versions[vid] = version
            name = version['file']
            safe_path(name)
            require(name not in paths and name not in SIDECARS, 'Duplicate or reserved asset path')
            paths.add(name)
            require(version['sha256'] == 'Unknown' or isinstance(version['sha256'], str) and DIGEST.fullmatch(version['sha256']), 'Invalid digest')
            size = version['pixel_size']
            require(size == 'Unknown' or isinstance(size, list) and len(size) == 2
                    and all(type(n) is int and n > 0 for n in size), 'Invalid actual pixel size')
            require(version['status'] in {'in_review', 'approved', 'rejected'}, 'Invalid version status')
            require(version['qa'] in {'pass', 'fail', 'Unknown'} and isinstance(version['qa_evidence'], str), 'Invalid QA record')
            if version['qa'] != 'Unknown':
                require(known_text(version['qa_evidence']), 'QA claim lacks evidence')
            origin = version['origin']
            require(origin['kind'] in {'newly_generated', 'extracted', 'reconstructed', 'authored_spec'}, 'Invalid origin')
            require(known_text(origin['note']) and isinstance(origin['source'], str), 'Missing origin explanation')
            if origin['kind'] in {'extracted', 'reconstructed'}:
                require(known_text(origin['source']), 'Separation requires its actual source reference')
            if asset['route'] == 'editable_text':
                require(origin['kind'] == 'authored_spec', 'Editable text must be an authored specification')
            else:
                require(origin['kind'] != 'authored_spec', 'Raster asset cannot be a text specification')
            if version['status'] == 'approved':
                approval = version['approval']
                require(isinstance(approval, dict) and known_text(approval['evidence']) and isinstance(approval['date'], str), 'Approval evidence missing')
            else:
                require(version['approval'] is None, 'Unapproved version carries approval')
            if version['status'] == 'in_review':
                pending.append(aid)
        selected = asset['selected_version']
        require(selected is None or selected in versions and versions[selected]['status'] == 'approved', 'Selected version is not approved')
    require(allocated == copy_ids, 'Project copy is missing an asset assignment')
    require(len(pending) <= 1, 'Sequential workflow allows one candidate in review')
    visiting, done = set(), set()
    def visit(aid):
        require(aid in by_id, 'Missing dependency: ' + aid)
        require(aid not in visiting, 'Cyclic asset dependency')
        if aid in done:
            return
        visiting.add(aid)
        for dep in by_id[aid]['depends_on']:
            visit(dep)
        visiting.remove(aid)
        done.add(aid)
    for aid in by_id:
        visit(aid)
    sequence = plan['sequence']
    require(isinstance(sequence, list) and sequence and len(sequence) == len(set(sequence)) and set(sequence) <= by_id.keys(), 'Invalid sequence scope')
    delivery = plan['delivery']
    require(delivery['choice'] in {'undecided', 'individual', 'zip'}, 'Invalid delivery choice')
    ids = delivery['asset_ids']
    require(isinstance(ids, list) and len(ids) == len(set(ids)) and set(ids) <= set(sequence), 'Invalid delivery subset')
    require(delivery['choice'] == 'undecided' or ids, 'Chosen delivery needs explicit asset IDs')
    if pending:
        return {'status': 'valid_plan', 'next_action': 'review_asset', 'asset_id': pending[0]}
    missing = next((aid for aid in sequence if by_id[aid]['selected_version'] is None), None)
    if missing:
        return {'status': 'valid_plan', 'next_action': 'create_asset', 'asset_id': missing}
    return {'status': 'valid_plan', 'next_action': 'choose_delivery' if delivery['choice'] == 'undecided' else 'verify_delivery'}


def inspect_file(path):
    path = Path(path)
    data = path.read_bytes()
    result = {'sha256': digest(data), 'bytes': len(data), 'pixel_size': 'Unknown', 'alpha': 'Unknown'}
    try:
        from PIL import Image
    except ImportError:
        return {**result, 'inspection': 'unavailable', 'reason': 'Pillow unavailable; no dependency installed'}
    try:
        with Image.open(path) as image:
            image.load()
            require(getattr(image, 'n_frames', 1) == 1, 'Animated file is not a static asset')
            result.update(pixel_size=list(image.size), format=image.format)
            has_alpha = 'A' in image.getbands() or 'transparency' in image.info
            if has_alpha:
                channel = image.convert('RGBA').getchannel('A')
                low, high = channel.getextrema()
                result.update(alpha='empty' if high == 0 else 'opaque' if low == 255 else 'transparent', alpha_extrema=[low, high], content_bbox=channel.getbbox())
            else:
                result.update(alpha='opaque', alpha_extrema=[255, 255])
        return {**result, 'inspection': 'measured', 'visual_qa': 'not_performed'}
    except (OSError, Image.DecompressionBombError) as exc:
        return {**result, 'inspection': 'unavailable', 'reason': str(exc)}


def portable_plan(plan):
    selected = set(plan['delivery']['asset_ids'])
    result = decode(json.dumps(plan))
    for asset in result['assets']:
        asset['versions'] = [v for v in asset['versions'] if asset['id'] in selected and v['id'] == asset['selected_version']]
        if asset['id'] not in selected:
            asset['selected_version'] = None
    # Undelivered assets keep design context, never file paths or approval history.
    result['sequence'] = [aid for aid in result['sequence'] if aid in selected]
    return result


def delivery_inventory(plan, root):
    decision = validate_plan(plan)
    require(decision['next_action'] == 'verify_delivery', 'Delivery requires resolved reviews, approved scoped assets and a user delivery choice')
    for key in ('width', 'height'):
        require(plan['canvas'][key] != 'Unknown', 'Delivery canvas unresolved')
    items = []
    for asset in plan['assets']:
        if asset['id'] not in plan['delivery']['asset_ids']:
            continue
        version = next(v for v in asset['versions'] if v['id'] == asset['selected_version'])
        require(version['qa'] == 'pass', 'Selected asset has unresolved/failed QA: ' + asset['id'])
        require(version['sha256'] != 'Unknown', 'Selected digest unmeasured')
        path = local_file(root, version['file'])
        require(digest(path.read_bytes()) == version['sha256'], 'Approved file bytes changed: ' + version['file'])
        require(all(v != 'Unknown' for v in asset['geometry'].values()), 'Asset placement unresolved')
        assigned_copy = [item for item in plan['composition']['copy'] if item['id'] in asset['copy_ids']]
        require(all(item['status'] == 'locked' and known_text(item['text']) for item in assigned_copy), 'Asset copy is not locked')
        if asset['route'] == 'raster':
            observed = inspect_file(path)
            require(observed['inspection'] == 'measured', 'Actual image inspection unavailable')
            require(observed['pixel_size'] == version['pixel_size'], 'Recorded pixel dimensions differ')
            require(observed['alpha'] != 'empty', 'Empty transparent asset')
            if asset['transparency'] in {'alpha', 'opaque'}:
                require(observed['alpha'] == ('transparent' if asset['transparency'] == 'alpha' else 'opaque'), 'Actual alpha differs from requirement')
            else:
                require(False, 'Raster transparency requirement unresolved')
            if asset['geometry']['canvas_mode'] == 'full_canvas':
                require(observed['pixel_size'] == [plan['canvas']['width'], plan['canvas']['height']], 'Full-canvas file dimensions differ')
        else:
            specification = path.read_text(encoding='utf-8')
            require(known_text(specification) and all(item['text'] in specification for item in assigned_copy), 'Text specification lost exact copy')
        items.append({'asset_id': asset['id'], 'version_id': version['id'], 'file': version['file'], 'sha256': version['sha256']})
    return {'project_id': plan['project_id'], 'revision': plan['revision'], 'assets': items}


def verify_delivery(plan, root, delivered):
    inventory = delivery_inventory(plan, root)
    target = Path(delivered)
    expected = {item['file']: item['sha256'] for item in inventory['assets']}
    names = set(expected) | SIDECARS
    source_sizes = {item['file']: local_file(root, item['file']).stat().st_size for item in inventory['assets']}
    def verify_bodies(read):
        for name, value in expected.items():
            require(digest(read(name)) == value, 'Delivered bytes differ: ' + name)
        require(decode(read('ASSET_INDEX.json')) == inventory, 'Delivery index differs from selected inventory')
        require(decode(read('layer-plan.json')) == portable_plan(plan), 'Delivered plan includes stale/unselected records or changed context')
        require(known_text(read('ASSEMBLY.md').decode('utf-8')), 'Empty assembly instructions')
    if target.is_dir():
        require(plan['delivery']['choice'] == 'individual', 'Directory delivery was not selected')
        entries = list(target.rglob('*'))
        require(all(not p.is_symlink() for p in entries), 'Symlink in delivered package')
        require({p.relative_to(target).as_posix() for p in entries if p.is_file()} == names, 'Delivered inventory differs')
        verify_bodies(lambda name: local_file(target, name).read_bytes())
    else:
        require(plan['delivery']['choice'] == 'zip', 'ZIP delivery was not selected')
        with zipfile.ZipFile(target) as archive:
            entries = archive.infolist()
            require(len(entries) == len(names) and {e.filename for e in entries} == names, 'ZIP inventory differs or contains duplicate entries')
            for entry in entries:
                safe_path(entry.filename)
                require(not entry.is_dir() and not stat.S_ISLNK(entry.external_attr >> 16) and not entry.flag_bits & 1, 'Unsafe/encrypted ZIP entry')
                require(entry.file_size == source_sizes[entry.filename] if entry.filename in source_sizes else entry.file_size <= 5_000_000, 'Unexpected ZIP entry size')
            verify_bodies(archive.read)
    return {'status': 'delivery_verified', 'assets': len(expected), 'files': len(names), 'format': plan['delivery']['choice'], 'visual_qa': 'not_performed'}


def compare(before, after):
    validate_plan(before)
    validate_plan(after)
    require(before['project_id'] == after['project_id'], 'Different projects')
    old, new = ({a['id']: a for a in p['assets']} for p in (before, after))
    ids = sorted(old.keys() | new.keys())
    return {'status': 'comparison_only', 'changed_assets': [i for i in ids if old.get(i) != new.get(i)],
            'changed_selections': [i for i in ids if old.get(i, {}).get('selected_version') != new.get(i, {}).get('selected_version')],
            'composition_changed': any(before[k] != after[k] for k in ('canvas', 'composition')),
            'authorization': 'not_established_by_comparison'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('check', 'inspect', 'compare', 'delivery', 'verify-delivery'):
        sub = commands.add_parser(name)
        sub.add_argument('input')
        if name == 'compare':
            sub.add_argument('after')
        if name in {'delivery', 'verify-delivery'}:
            sub.add_argument('--root', required=True)
        if name == 'verify-delivery':
            sub.add_argument('--delivered', required=True)
    args = parser.parse_args()
    try:
        if args.command == 'inspect':
            result = inspect_file(args.input)
        else:
            plan = load(args.input)
            result = (validate_plan(plan) if args.command == 'check' else
                      compare(plan, load(args.after)) if args.command == 'compare' else
                      delivery_inventory(plan, args.root) if args.command == 'delivery' else
                      verify_delivery(plan, args.root, args.delivered))
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError, zipfile.BadZipFile, RuntimeError) as exc:
        print(json.dumps({'status': 'verification_failed', 'error': str(exc)}))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
