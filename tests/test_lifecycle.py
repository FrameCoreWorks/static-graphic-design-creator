"""Exercise installation/update proposals on disposable bytes and directories."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.agents/skills/static-graphic-design-creator/scripts'))
import skill_lifecycle as life
spec = importlib.util.spec_from_file_location('release', ROOT / 'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


def record(version):
    return json.dumps({'repository': life.REPOSITORY, 'skill_name': life.NAME, 'version': version,
                       'release_id': 'v' + version, 'release_channel': 'candidate'}).encode()


def sample(version='1.0', **entries):
    return {'SKILL.md': b'Example source', life.RECORD: record(version), **{k: v.encode() for k, v in entries.items()}}


def manifest(files, source='a' * 40):
    original = life.parse_json((ROOT / release.MANIFEST).read_bytes())
    r = life.parse_json(files[life.RECORD])
    original.update(version=r['version'], release_id=r['release_id'], immutable_source_commit=source, ref=source)
    original['skills'][0]['files'] = [
        {'path': p, 'repository_path': life.SOURCE_ROOT + '/' + p,
         'raw_url': release.RAW + source + '/' + life.SOURCE_ROOT + '/' + p, 'sha256': life.sha(data)}
        for p, data in files.items()]
    return original


def bootstrap(m):
    config = life.parse_json((ROOT / release.BOOTSTRAP).read_bytes())
    config['version'] = m['version']
    config['release'].update(id=m['release_id'], channel=m['release_channel'], immutable_source_commit=m['ref'])
    return config


def write_files(root, files):
    for path, data in files.items():
        p = root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)


class LifecycleTests(unittest.TestCase):
    def test_fresh_install_update_and_second_update_are_exact(self):
        first = sample(a='old', obsolete='remove')
        second = sample('2.0', a='new', added='new file')
        life.verify_bundle(dict(first), manifest(first))
        plan = life.compare(first, second, first)
        self.assertEqual(plan['status'], 'ready_for_review')
        updated = life.build_proposal(first, second, first)
        self.assertEqual(updated, second)
        self.assertNotIn('obsolete', updated)
        life.verify_result(updated, dict(updated))
        self.assertEqual(life.compare(second, second, updated)['status'], 'already_up_to_date')

    def test_extension_survives_two_source_updates_without_core_collision(self):
        first = sample(a='old')
        installed = {**first, 'local/SKILL_EXTENSIONS.md': b'Approved local behavior', 'assets/icon.svg': b'icon'}
        second = sample('2.0', a='new')
        updated = life.build_proposal(first, second, installed)
        self.assertEqual(updated['local/SKILL_EXTENSIONS.md'], installed['local/SKILL_EXTENSIONS.md'])
        self.assertEqual(life.compare(second, second, updated)['status'], 'local_customizations_preserved')
        third = sample('3.0', a='third')
        final = life.build_proposal(second, third, updated)
        self.assertEqual(final, {**third, 'local/SKILL_EXTENSIONS.md': b'Approved local behavior', 'assets/icon.svg': b'icon'})

    def test_real_legacy_extension_conflicts_and_reviewed_adoption(self):
        def from_git(commit):
            return release.source_files(commit)
        base = from_git('67a48cb7589d894959f39fdbe37ce647499d657c')
        target = from_git('aed4bb2566e9b408e2e34d78b35b30a4c07d2348')
        installed = dict(target)
        installed[life.RECORD] = base[life.RECORD]
        collisions = ['references/evaluation-scenarios.md', 'references/event-poster-code-workflow.md',
                      'references/event-poster-design-codes.json', 'scripts/event_poster_codes.py']
        for path in collisions:
            # Same semantic catalog/helper, different development provenance text.
            installed[path] = target[path] + b'\n'
        installed['agents/openai.yaml'] += b'\n# Host customization\n'
        installed['assets/icon.svg'] = b'<svg/>'
        untouched = dict(installed)
        plan = life.compare(base, target, installed)
        self.assertEqual((len(plan['already_target']), len(plan['target_deviations'])), (18, 7))
        self.assertEqual(set(plan['delta']['conflicts']), set(collisions))
        self.assertEqual(plan['apply_mode'], 'none')
        self.assertEqual(set(plan['conflict_previews']), set(collisions))
        self.assertTrue(all(p['kind'] == 'add_add' for p in plan['conflict_previews'].values()))
        with self.assertRaises(ValueError):
            life.build_proposal(base, target, installed)
        adopted = life.build_proposal(base, target, installed, {p: 'target' for p in collisions})
        self.assertEqual(installed, untouched)  # Neither review nor proposal mutates the installation.
        self.assertEqual(adopted[life.RECORD], target[life.RECORD])
        self.assertEqual(adopted['agents/openai.yaml'], installed['agents/openai.yaml'])
        self.assertEqual(adopted['assets/icon.svg'], installed['assets/icon.svg'])
        self.assertEqual(life.compare(target, target, adopted)['status'], 'local_customizations_preserved')

    def test_stale_record_only_is_a_reviewed_metadata_update(self):
        base, target = sample(), sample('2.0')
        plan = life.compare(base, target, base)
        self.assertEqual(plan['delta']['apply'], [life.RECORD])
        self.assertTrue(plan['approval_required_before_save'])
        self.assertEqual(life.build_proposal(base, target, base), target)

    def test_conflict_cannot_partially_advance_source_record(self):
        base, target = sample(a='base'), sample('2.0', a='target')
        installed = {**base, 'a': b'local'}
        with self.assertRaises(ValueError):
            life.build_proposal(base, target, installed)
        self.assertEqual(installed[life.RECORD], base[life.RECORD])
        merged = life.build_proposal(base, target, installed, {'a': b'reviewed merge'})
        self.assertEqual(merged['a'], b'reviewed merge')
        self.assertEqual(merged[life.RECORD], target[life.RECORD])

    def test_modified_obsolete_file_requires_resolution(self):
        base, target = sample(old='source'), sample('2.0')
        installed = {**base, 'old': b'personal'}
        self.assertEqual(life.compare(base, target, installed)['delta']['conflicts'], ['old'])
        preserved = life.build_proposal(base, target, installed, {'old': 'local'})
        self.assertEqual(preserved['old'], b'personal')
        removed = life.build_proposal(base, target, installed, {'old': 'target'})
        self.assertNotIn('old', removed)

    def test_changed_input_failed_readback_and_rollback_are_detectable(self):
        base, target = sample(a='base'), sample('2.0', a='new')
        proposal = life.build_proposal(base, target, base)
        with self.assertRaises(ValueError):
            life.verify_result(base, {**base, 'a': b'concurrent edit'})
        with self.assertRaises(ValueError):
            life.verify_result(proposal, {**proposal, life.RECORD: base[life.RECORD]})
        with self.assertRaises(ValueError):
            life.verify_result(proposal, {**proposal, 'leftover': b'old source'})
        life.verify_result(base, dict(base))  # Restored snapshot, checked including the old record.

    def test_foreign_missing_or_wrong_baseline_is_rejected(self):
        base, target = sample(), sample('2.0')
        for installed in [sample('3.0'), {'SKILL.md': b'x'}, {**base, life.RECORD: record('1.0').replace(b'FrameCoreWorks', b'ForeignOwner')}]:
            with self.assertRaises(ValueError):
                life.compare(base, target, installed)

    def test_manifest_and_bootstrap_reject_mixed_identity(self):
        files = sample()
        m = manifest(files)
        for mutate in [lambda c: c.update(repository='https://example.com'),
                       lambda c: c['skills'][0].update(source_root='elsewhere'),
                       lambda c: c['skills'][0].update(files=[]),
                       lambda c: c['release'].update(channel='stable')]:
            c = bootstrap(m)
            mutate(c)
            with self.assertRaises(ValueError):
                life.validate_bootstrap(c, m)
        for changed in [{**files, 'extra': b'x'}, {**files, 'SKILL.md': b'wrong'}]:
            with self.assertRaises(ValueError):
                life.verify_bundle(changed, m)
        private = {**files, 'local/SKILL_EXTENSIONS.md': b'private'}
        with self.assertRaises(ValueError):
            life.verify_bundle(private, manifest(private))

    def test_read_only_cli_and_unsafe_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            files = sample()
            for name in ('base', 'target', 'installed'):
                write_files(root / name, files)
            mf = root / 'manifest.json'
            mf.write_text(json.dumps(manifest(files)))
            before = life.read_tree(root)
            result = subprocess.run([sys.executable, '-B', str(Path(life.__file__)), '--baseline', str(root / 'base'),
                                     '--target', str(root / 'target'), '--installed', str(root / 'installed'),
                                     '--baseline-manifest', str(mf), '--target-manifest', str(mf)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout)['status'], 'already_up_to_date')
            self.assertEqual(before, life.read_tree(root))
            (root / 'installed/escape').symlink_to(mf)
            with self.assertRaises(ValueError):
                life.read_tree(root / 'installed')


class ReleaseTests(unittest.TestCase):
    def test_historical_baselines_and_mismatched_locator(self):
        history = life.parse_json((ROOT / release.HISTORY).read_bytes())
        self.assertGreaterEqual(release.validate_history(history), 5)
        wrong = copy.deepcopy(history)
        wrong['releases'][0]['manifest_commit'] = wrong['releases'][1]['manifest_commit']
        with self.assertRaises(ValueError):
            release.validate_history(wrong)

    def test_lock_uses_exact_committed_source_and_rejects_dirty_or_published_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            subprocess.run(['git', '-C', str(root), 'config', 'user.name', 'Test'], check=True)
            subprocess.run(['git', '-C', str(root), 'config', 'user.email', 'test@example.invalid'], check=True)
            files = sample('99.0', added='keep')
            write_files(root / life.SOURCE_ROOT, files)
            write_files(root, {release.MANIFEST: json.dumps(manifest(files)).encode(),
                               release.BOOTSTRAP: json.dumps(bootstrap(manifest(files))).encode(),
                               'EVALUATION.md': b'1. Example: perform a host test.\n'})
            subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(root), 'commit', '-qm', 'Source'], check=True)
            source = release.git('rev-parse', 'HEAD', root=root).decode().strip()
            result = release.prepare_lock(source, root)
            self.assertEqual(result['files'], 3)
            m = life.parse_json((root / release.MANIFEST).read_bytes())
            life.verify_bundle(files, m)
            life.validate_bootstrap(life.parse_json((root / release.BOOTSTRAP).read_bytes()), m)
            (root / life.SOURCE_ROOT / 'added').write_bytes(b'dirty')
            before = (root / release.MANIFEST).read_bytes()
            with self.assertRaises(ValueError):
                release.prepare_lock(source, root)
            self.assertEqual(before, (root / release.MANIFEST).read_bytes())
            (root / life.SOURCE_ROOT / 'added').write_bytes(b'keep')
            subprocess.run(['git', '-C', str(root), 'tag', 'v99.0'], check=True)
            with self.assertRaises(ValueError):
                release.prepare_lock(source, root)

    def public_fixture(self):
        files, lock = sample(), 'b' * 40
        m = manifest(files)
        encode = lambda d: json.dumps(d).encode()
        data = {
            release.RAW + lock + '/' + release.MANIFEST: encode(m),
            release.RAW + lock + '/' + release.BOOTSTRAP: encode(bootstrap(m)),
            release.RAW + 'v1.0/' + release.MANIFEST: encode(m),
            release.RAW + 'v1.0/' + release.BOOTSTRAP: encode(bootstrap(m)),
            release.API + '/commits/main': encode({'sha': lock}),
            release.API + '/commits/v1.0': encode({'sha': lock}),
            release.API + '/compare/' + m['ref'] + '...' + lock: encode({'status': 'ahead'}),
            release.API + '/git/trees/' + m['ref'] + '?recursive=1': encode({'truncated': False, 'tree': [
                {'path': life.SOURCE_ROOT + '/' + p, 'type': 'blob', 'mode': '100644'} for p in files]}),
            release.API + '/actions/workflows/validate.yml/runs?head_sha=' + lock + '&event=push&per_page=20': encode({
                'workflow_runs': [{'head_sha': lock, 'event': 'push', 'head_branch': 'main', 'id': 1,
                                   'status': 'completed', 'conclusion': 'success'}]}),
        }
        data.update({entry['raw_url']: files[entry['path']] for entry in m['skills'][0]['files']})
        return lock, m, data

    def test_public_verification_covers_refs_source_inventory_bytes_and_ci(self):
        lock, m, data = self.public_fixture()
        result = release.verify_public(lock, 'v1.0', data.__getitem__)
        self.assertEqual(result['status'], 'public_release_verified')
        bad_values = {
            release.API + '/commits/main': json.dumps({'sha': 'c' * 40}).encode(),
            release.API + '/commits/v1.0': json.dumps({'sha': 'c' * 40}).encode(),
            m['skills'][0]['files'][0]['raw_url']: b'wrong bytes',
            release.RAW + 'v1.0/' + release.MANIFEST: b'{}',
            release.API + '/compare/' + m['ref'] + '...' + lock: b'{"status":"diverged"}',
            release.API + '/git/trees/' + m['ref'] + '?recursive=1': b'{"truncated":true,"tree":[]}',
        }
        for url, bad in bad_values.items():
            with self.subTest(url=url), self.assertRaises(ValueError):
                release.verify_public(lock, 'v1.0', {**data, url: bad}.__getitem__)
        ci_url = next(u for u in data if '/actions/' in u)
        for conclusion in ['failure', None]:
            ci = json.loads(data[ci_url]); ci['workflow_runs'][0]['conclusion'] = conclusion
            with self.assertRaises(ValueError):
                release.verify_public(lock, 'v1.0', {**data, ci_url: json.dumps(ci).encode()}.__getitem__)
        ci = json.loads(data[ci_url]); ci['workflow_runs'].append({**ci['workflow_runs'][0], 'id': 2, 'conclusion': 'failure'})
        with self.assertRaises(ValueError):
            release.verify_public(lock, 'v1.0', {**data, ci_url: json.dumps(ci).encode()}.__getitem__)


if __name__ == '__main__':
    unittest.main()
