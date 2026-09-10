"""Deterministic checks with synthetic disposable files, never live image/host evidence."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from PIL import Image

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))
import layer_assets as layers


class LayerAssetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plan = layers.load(SKILL / 'templates/layer-plan.json')
        self.plan['canvas'] = {'width': 32, 'height': 48}
        for a in self.plan['assets']:
            a['geometry'].update(width=32, height=48)

    def version(self, index, vid='v001', status='approved', alpha=None):
        asset = self.plan['assets'][index]
        text = asset['route'] == 'editable_text'
        name = asset['id'] + '-' + vid + ('.md' if text else '.png')
        path = self.root / name
        if text:
            path.write_text('Title: AFTER HOURS\nTop quarter, upright display sans, centered.\n')
        else:
            desired = alpha or asset['transparency']
            image = Image.new('RGBA', (32, 48), (20, 30, 40, 255 if desired == 'opaque' else 0))
            if desired == 'alpha':
                image.putpixel((16, 24), (100, 150, 200, 180))
            image.save(path)
        v = {'id': vid, 'file': name, 'sha256': layers.digest(path.read_bytes()),
             'pixel_size': 'Unknown' if text else [32, 48], 'status': status,
             'qa': 'pass', 'qa_evidence': 'Synthetic fixture checked by test construction',
             'approval': {'evidence': 'Synthetic user acceptance for this fixture only', 'date': '2026-09-10'} if status == 'approved' else None,
             'origin': {'kind': 'authored_spec' if text else 'newly_generated', 'source': 'Synthetic test fixture', 'note': 'Not actual model output or user approval'}}
        asset['versions'].append(v)
        if status == 'approved':
            asset['selected_version'] = vid
        return v

    def complete(self, choice='zip'):
        for i in range(len(self.plan['assets'])):
            self.version(i)
        self.plan['delivery'] = {'choice': choice, 'asset_ids': list(self.plan['sequence'])}

    def package(self, extras=None, directory=False):
        index = layers.delivery_inventory(self.plan, self.root)
        bodies = {v['file']: (self.root / v['file']).read_bytes() for v in index['assets']}
        bodies.update({'ASSET_INDEX.json': json.dumps(index).encode(),
                       'layer-plan.json': json.dumps(layers.portable_plan(self.plan)).encode(),
                       'ASSEMBLY.md': b'32 x 48. Background, person with shadow, fog, manual title at top. Normal alpha-over.'})
        bodies.update(extras or {})
        target = self.root / ('delivered' if directory else 'approved.zip')
        if directory:
            target.mkdir()
            for name, body in bodies.items():
                (target / name).write_bytes(body)
        else:
            with zipfile.ZipFile(target, 'w') as archive:
                for name, body in bodies.items():
                    archive.writestr(name, body)
        return target

    def test_actual_template_is_unrendered_starting_plan(self):
        plan = layers.load(SKILL / 'templates/layer-plan.json')
        self.assertEqual(layers.validate_plan(plan)['asset_id'], 'background')
        self.assertTrue(all(a['selected_version'] is None and not a['versions'] for a in plan['assets']))

    def test_review_stops_sequence_until_explicit_selection(self):
        v = self.version(0, status='in_review')
        self.assertEqual(layers.validate_plan(self.plan)['next_action'], 'review_asset')
        v.update(status='approved', approval={'evidence': 'Synthetic acceptance', 'date': 'Unknown'})
        self.plan['assets'][0]['selected_version'] = v['id']
        self.assertEqual(layers.validate_plan(self.plan)['asset_id'], 'person')

    def test_two_simultaneous_reviews_rejected(self):
        self.version(0, status='in_review')
        self.version(1, status='in_review')
        with self.assertRaisesRegex(ValueError, 'one candidate'):
            layers.validate_plan(self.plan)

    def test_replacement_preserves_selection_during_review(self):
        self.complete()
        before = copy.deepcopy(self.plan)
        self.version(1, 'v002', status='in_review')
        self.assertEqual(self.plan['assets'][1]['selected_version'], 'v001')
        delta = layers.compare(before, self.plan)
        self.assertEqual(delta['changed_assets'], ['person'])
        self.assertEqual(delta['changed_selections'], [])
        with self.assertRaisesRegex(ValueError, 'resolved reviews'):
            layers.delivery_inventory(self.plan, self.root)

    def test_rejected_latest_version_is_never_packaged(self):
        self.complete()
        rejected = self.version(1, 'v009', status='rejected')
        target = self.package()
        self.assertEqual(layers.verify_delivery(self.plan, self.root, target)['assets'], 4)
        with zipfile.ZipFile(target) as archive:
            self.assertNotIn(rejected['file'], archive.namelist())
            self.assertNotIn('v009', archive.read('layer-plan.json').decode())

    def test_new_selection_changes_only_that_asset(self):
        self.complete()
        before = copy.deepcopy(self.plan)
        self.version(1, 'v002')
        delta = layers.compare(before, self.plan)
        self.assertEqual(delta['changed_selections'], ['person'])
        self.assertFalse(delta['composition_changed'])
        self.assertEqual(before['assets'][0], self.plan['assets'][0])

    def test_approval_or_qa_cannot_be_prefilled_without_evidence(self):
        v = self.version(0)
        for field, value in [('approval', None), ('qa_evidence', 'Unknown')]:
            plan = copy.deepcopy(self.plan)
            plan['assets'][0]['versions'][0][field] = value
            with self.assertRaises(ValueError):
                layers.validate_plan(plan)
        v['status'] = 'rejected'
        v['approval'] = None
        with self.assertRaisesRegex(ValueError, 'not approved'):
            layers.validate_plan(self.plan)

    def test_duplicate_ids_paths_and_stack_order_rejected(self):
        self.version(0)
        self.version(1)
        for change in ('id', 'z_index', 'file'):
            plan = copy.deepcopy(self.plan)
            if change == 'file':
                plan['assets'][1]['versions'][0]['file'] = plan['assets'][0]['versions'][0]['file']
            else:
                plan['assets'][1][change] = plan['assets'][0][change]
            with self.assertRaises(ValueError):
                layers.validate_plan(plan)

    def test_dependency_cycles_and_missing_dependencies_rejected(self):
        for deps in (['fog'], ['missing']):
            self.plan['assets'][0]['depends_on'] = deps
            with self.assertRaises(ValueError):
                layers.validate_plan(self.plan)

    def test_lost_copy_mapping_rejected(self):
        self.plan['assets'][3]['copy_ids'] = []
        with self.assertRaisesRegex(ValueError, 'copy is missing'):
            layers.validate_plan(self.plan)

    def test_unresolved_title_does_not_block_independent_background(self):
        self.plan['composition']['copy'][0].update(text='', status='draft', source='Unknown')
        self.plan['sequence'] = ['background']
        self.version(0)
        self.plan['delivery'] = {'choice': 'individual', 'asset_ids': ['background']}
        self.assertEqual(len(layers.delivery_inventory(self.plan, self.root)['assets']), 1)

    def test_structured_concept_and_copy_authority_survive_handoff(self):
        lock = {'premise': 'Night event', 'mechanism': 'Warm person in cool square',
                'distinctive_hook': 'Human warmth interrupts empty space',
                'allowed_adaptations': ['Asset placement within agreed bounds'],
                'forbidden_substitutions': ['Generic city skyline'], 'source_context': {'brief_id': 'approved-brief'}}
        self.plan['composition']['concept_lock'] = lock
        self.plan['composition']['copy'][0].update(required=True, authority='user_locked', allowed_changes='layout_only')
        self.complete()
        portable = layers.portable_plan(self.plan)
        layers.validate_plan(portable)
        self.assertEqual(portable['composition'], self.plan['composition'])
        self.assertEqual(portable['composition']['concept_lock'], lock)

    def test_editable_spec_preserves_exact_copy(self):
        self.complete()
        v = self.plan['assets'][3]['versions'][0]
        (self.root / v['file']).write_text('Wrong title')
        v['sha256'] = layers.digest((self.root / v['file']).read_bytes())
        with self.assertRaisesRegex(ValueError, 'lost exact copy'):
            layers.delivery_inventory(self.plan, self.root)

    def test_unknown_canvas_permitted_for_planning_not_delivery(self):
        self.plan['canvas']['width'] = 'Unknown'
        for a in self.plan['assets']:
            a['geometry']['width'] = 'Unknown'
        layers.validate_plan(self.plan)
        self.complete()
        with self.assertRaisesRegex(ValueError, 'canvas unresolved'):
            layers.delivery_inventory(self.plan, self.root)

    def test_opaque_checkerboard_is_not_alpha(self):
        self.complete()
        v = self.plan['assets'][1]['versions'][0]
        image = Image.new('RGB', (32, 48), 'white')
        for x in range(32):
            for y in range(48):
                image.putpixel((x, y), (160, 160, 160) if (x // 4 + y // 4) % 2 else (255, 255, 255))
        image.save(self.root / v['file'])
        v['sha256'] = layers.digest((self.root / v['file']).read_bytes())
        self.assertEqual(layers.inspect_file(self.root / v['file'])['alpha'], 'opaque')
        with self.assertRaisesRegex(ValueError, 'alpha differs'):
            layers.delivery_inventory(self.plan, self.root)

    def test_empty_alpha_fails_delivery(self):
        self.complete()
        v = self.plan['assets'][1]['versions'][0]
        Image.new('RGBA', (32, 48), (0, 0, 0, 0)).save(self.root / v['file'])
        v['sha256'] = layers.digest((self.root / v['file']).read_bytes())
        with self.assertRaisesRegex(ValueError, 'Empty transparent'):
            layers.delivery_inventory(self.plan, self.root)

    def test_palette_transparency_is_detected(self):
        p = self.root / 'palette.png'
        image = Image.new('P', (4, 4), 0)
        image.putpixel((1, 1), 1)
        image.save(p, transparency=0)
        self.assertEqual(layers.inspect_file(p)['alpha'], 'transparent')

    def test_corrupt_image_is_not_verified(self):
        p = self.root / 'broken.png'
        p.write_bytes(b'not an image')
        self.assertEqual(layers.inspect_file(p)['inspection'], 'unavailable')

    def test_missing_pillow_reports_unavailable(self):
        self.version(0)
        with patch.dict(sys.modules, {'PIL': None}):
            result = layers.inspect_file(self.root / 'background-v001.png')
        self.assertEqual(result['alpha'], 'Unknown')
        self.assertEqual(result['inspection'], 'unavailable')

    def test_actual_dimensions_must_match_registry_and_full_canvas(self):
        self.complete()
        v = self.plan['assets'][0]['versions'][0]
        v['pixel_size'] = [1, 1]
        with self.assertRaisesRegex(ValueError, 'pixel dimensions differ'):
            layers.delivery_inventory(self.plan, self.root)
        v['pixel_size'] = [32, 48]
        self.plan['canvas']['width'] = 64
        for a in self.plan['assets']:
            a['geometry']['width'] = 64
        with self.assertRaisesRegex(ValueError, 'Full-canvas file dimensions differ'):
            layers.delivery_inventory(self.plan, self.root)

    def test_cropped_file_has_independent_placement(self):
        self.complete()
        self.plan['assets'][1]['geometry'].update(canvas_mode='cropped', x=8, y=12, width=16, height=24)
        self.assertEqual(len(layers.delivery_inventory(self.plan, self.root)['assets']), 4)

    def test_origin_requires_source_and_truthful_route(self):
        v = self.version(0)
        v['origin'].update(kind='extracted', source='Unknown')
        with self.assertRaisesRegex(ValueError, 'actual source'):
            layers.validate_plan(self.plan)
        v['origin']['source'] = 'uploaded-poster.png'
        layers.validate_plan(self.plan)
        v['origin']['kind'] = 'authored_spec'
        with self.assertRaisesRegex(ValueError, 'Raster asset'):
            layers.validate_plan(self.plan)

    def test_delivery_choice_is_not_inferred(self):
        self.complete()
        self.plan['delivery'] = {'choice': 'undecided', 'asset_ids': []}
        self.assertEqual(layers.validate_plan(self.plan)['next_action'], 'choose_delivery')
        with self.assertRaises(ValueError):
            layers.delivery_inventory(self.plan, self.root)

    def test_changed_or_missing_approved_bytes_block_delivery(self):
        self.complete()
        path = self.root / 'background-v001.png'
        path.write_bytes(path.read_bytes() + b'drift')
        with self.assertRaisesRegex(ValueError, 'bytes changed'):
            layers.delivery_inventory(self.plan, self.root)
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'Missing'):
            layers.delivery_inventory(self.plan, self.root)

    def test_symlinks_and_escaping_paths_rejected(self):
        for path in ('../private', '/absolute', 'a/../b', 'a//b', './a', 'a\\b', 'C:secret', 'a\x00b'):
            with self.assertRaises(ValueError):
                layers.safe_path(path)
        (self.root / 'link').symlink_to(SKILL / 'SKILL.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            layers.local_file(self.root, 'link')

    def test_zip_extra_or_changed_asset_rejected(self):
        self.complete()
        for extras in ({'rejected.png': b'draft'}, {'background-v001.png': b'replaced'}):
            target = self.package(extras)
            with self.assertRaises(ValueError):
                layers.verify_delivery(self.plan, self.root, target)

    def test_zip_duplicate_and_stale_sidecar_rejected(self):
        self.complete()
        target = self.package({'ASSET_INDEX.json': b'{}'})
        with self.assertRaisesRegex(ValueError, 'index differs'):
            layers.verify_delivery(self.plan, self.root, target)
        target = self.package()
        with zipfile.ZipFile(target, 'a') as archive:
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', UserWarning)
                archive.writestr('ASSEMBLY.md', b'duplicate')
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            layers.verify_delivery(self.plan, self.root, target)

    def test_subset_delivery_plan_remains_valid_without_draft_files(self):
        self.complete()
        self.plan['delivery']['asset_ids'] = ['person']
        portable = layers.portable_plan(self.plan)
        layers.validate_plan(portable)
        self.assertTrue(all(not a['versions'] for a in portable['assets'] if a['id'] != 'person'))
        self.assertEqual(layers.verify_delivery(self.plan, self.root, self.package())['assets'], 1)

    def test_individual_delivery_exact_inventory(self):
        self.complete('individual')
        folder = self.package(directory=True)
        self.assertEqual(layers.verify_delivery(self.plan, self.root, folder)['files'], 7)
        (folder / 'unexpected.txt').write_text('extra')
        with self.assertRaisesRegex(ValueError, 'inventory differs'):
            layers.verify_delivery(self.plan, self.root, folder)

    def test_qa_failure_blocks_verified_package(self):
        self.complete()
        self.plan['assets'][1]['versions'][0]['qa'] = 'fail'
        with self.assertRaisesRegex(ValueError, 'failed QA'):
            layers.delivery_inventory(self.plan, self.root)

    def test_cli_read_only_and_invalid_json_errors(self):
        path = self.root / 'plan.json'
        path.write_text(json.dumps(self.plan))
        before = path.read_bytes()
        result = subprocess.run([sys.executable, '-B', str(SKILL / 'scripts/layer_assets.py'), 'check', str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)['asset_id'], 'background')
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(set(p.name for p in self.root.iterdir()), {'plan.json'})
        path.write_text('{"schema_version":1,"schema_version":2}')
        result = subprocess.run([sys.executable, '-B', str(SKILL / 'scripts/layer_assets.py'), 'check', str(path)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)['status'], 'verification_failed')
        with self.assertRaises(ValueError):
            layers.decode('{"opacity":NaN}')


if __name__ == '__main__':
    unittest.main()
