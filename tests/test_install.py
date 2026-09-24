import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'starter with spaces'
        shutil.copytree(PROJECT, self.repo, ignore=shutil.ignore_patterns('.sources', '.state', '.git', '__pycache__'))
        self.home = self.base / 'home'
        self.home.mkdir()

    def run_cli(self, *args, expected=0):
        p = subprocess.run([sys.executable, str(self.repo / 'install.py'), '--home', str(self.home), *args],
                           text=True, capture_output=True)
        self.assertEqual(p.returncode, expected, p.stdout + p.stderr)
        return p

    def links(self, name='cmux-orchestrate'):
        return [self.home / x / name for x in ['.claude/skills', '.agents/skills']]

    def test_preview_and_check_never_write(self):
        self.run_cli()
        self.run_cli('--check', expected=1)
        self.assertEqual(list(self.home.iterdir()), [])
        self.assertFalse((self.repo / '.state').exists())

    def test_apply_idempotence_and_uninstall(self):
        self.run_cli('--apply')
        for link in self.links():
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.resolve(), self.repo / 'skills/cmux-orchestrate')
        self.run_cli('--check')
        self.assertIn('0 link changes', self.run_cli('--apply').stdout)
        self.run_cli('--uninstall')
        self.assertTrue(all(p.is_symlink() for p in self.links()))
        self.run_cli('--uninstall', '--apply')
        self.assertTrue(all(not p.is_symlink() for p in self.links()))
        self.assertTrue((self.repo / 'skills/cmux-orchestrate/SKILL.md').exists())

    def test_foreign_directory_blocks_whole_plan(self):
        foreign = self.links()[1]
        foreign.mkdir(parents=True)
        (foreign / 'keep').write_text('mine')
        self.run_cli('--apply', expected=2)
        self.assertFalse(self.links()[0].exists())
        self.assertEqual((foreign / 'keep').read_text(), 'mine')

    def test_foreign_dangling_link_is_preserved(self):
        foreign = self.links()[0]
        foreign.parent.mkdir(parents=True)
        foreign.symlink_to(self.base / 'missing')
        self.run_cli('--apply', expected=2)
        self.assertTrue(foreign.is_symlink())

    def test_modified_owned_link_blocks_uninstall(self):
        self.run_cli('--apply')
        modified = self.links()[1]
        modified.unlink()
        modified.write_text('user replacement')
        self.run_cli('--uninstall', '--apply', expected=2)
        self.assertTrue(self.links()[0].is_symlink())
        self.assertEqual(modified.read_text(), 'user replacement')

    def test_legacy_codex_collision(self):
        old = self.home / '.codex/skills/cmux-orchestrate'
        old.mkdir(parents=True)
        self.run_cli('--apply', expected=2)
        self.assertFalse(self.links()[0].exists())

    def test_single_harness_and_custom_target(self):
        dest = self.home / 'custom'
        self.run_cli('--harness', 'codex', '--codex-dir', str(dest), '--apply')
        self.assertTrue((dest / 'cmux-orchestrate').is_symlink())
        self.assertFalse(self.links()[0].exists())
        self.run_cli('--harness', 'codex', '--codex-dir', str(dest), '--check')

    def test_symlinked_parent_requires_explicit_real_path(self):
        (self.home / '.claude').symlink_to(self.base)
        self.run_cli('--apply', expected=2)
        self.assertFalse((self.base / 'skills').exists())

    def test_unknown_skill_and_duplicate_rejected(self):
        self.run_cli('--skills', '../other', expected=2)
        self.run_cli('--skills', 'cmux-orchestrate', 'cmux-orchestrate', expected=2)

    def fixture_source(self):
        source = self.base / 'source'
        (source / 'skills/autoreview').mkdir(parents=True)
        (source / 'skills/autoreview/SKILL.md').write_text('---\nname: autoreview\ndescription: Test fixture\n---\n')
        subprocess.run(['git', 'init', '-q', str(source)], check=True)
        subprocess.run(['git', '-C', str(source), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(source), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                        '-c', 'commit.gpgsign=false', '-c', 'core.hooksPath=/dev/null', 'commit', '-qm', 'fixture'], check=True)
        pin = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
        manifest_path = self.repo / 'sources.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['sources']['agent-skills'].update(url=str(source), revision=pin)
        manifest_path.write_text(json.dumps(manifest))
        return source

    def test_reuse_source_and_detect_dirty_source(self):
        source = self.fixture_source()
        self.run_cli('--skills', 'autoreview', '--source', f'agent-skills={source}', '--apply')
        self.run_cli('--skills', 'autoreview', '--check')
        self.assertEqual(self.links('autoreview')[0].resolve(), source / 'skills/autoreview')
        (source / 'new-file').write_text('work')
        self.run_cli('--skills', 'autoreview', '--check', expected=2)
        self.run_cli('--skills', 'autoreview', '--uninstall', '--apply')
        self.assertEqual((source / 'new-file').read_text(), 'work')

    def test_fetch_pin_and_share_one_source(self):
        self.fixture_source()
        self.run_cli('--skills', 'autoreview', '--apply')
        links = self.links('autoreview')
        self.assertEqual(links[0].resolve(), links[1].resolve())
        self.run_cli('--skills', 'autoreview', '--check')

    def test_wrong_pin_blocks_before_loader_changes(self):
        source = self.fixture_source()
        path = self.repo / 'sources.json'
        manifest = json.loads(path.read_text())
        manifest['sources']['agent-skills']['revision'] = '0' * 40
        path.write_text(json.dumps(manifest))
        self.run_cli('--skills', 'autoreview', '--source', f'agent-skills={source}', '--apply', expected=2)
        self.assertFalse(self.links('autoreview')[0].exists())

    def test_partial_owner_upgrade_refused_then_full_upgrade_converges(self):
        source = self.fixture_source()
        (source / 'skills/handoff').mkdir()
        (source / 'skills/handoff/SKILL.md').write_text('fixture')
        def commit(message):
            subprocess.run(['git', '-C', str(source), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(source), '-c', 'user.name=Fixture',
                            '-c', 'user.email=fixture@example.invalid', '-c', 'commit.gpgsign=false',
                            '-c', 'core.hooksPath=/dev/null', 'commit', '-qm', message], check=True)
            pin = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
            path = self.repo / 'sources.json'
            manifest = json.loads(path.read_text())
            manifest['sources']['agent-skills']['revision'] = pin
            path.write_text(json.dumps(manifest))
        commit('add handoff')
        self.run_cli('--skills', 'autoreview', 'handoff', '--apply')
        old = self.links('handoff')[0].resolve()
        (source / 'skills/handoff/SKILL.md').write_text('changed fixture')
        commit('update')
        self.run_cli('--skills', 'autoreview', '--apply', expected=2)
        self.assertEqual(self.links('handoff')[0].resolve(), old)
        self.run_cli('--skills', 'autoreview', 'handoff', '--apply')
        self.run_cli('--skills', 'autoreview', 'handoff', '--check')
        self.assertNotEqual(self.links('handoff')[0].resolve(), old)

    def test_handled_failure_rolls_back_link_mutations(self):
        spec = importlib.util.spec_from_file_location('isolated_installer', self.repo / 'install.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with patch.object(sys, 'argv', ['install.py', '--home', str(self.home), '--apply']), \
             patch.object(module, 'write_state', side_effect=OSError('fixture disk failure')):
            self.assertEqual(module.main(), 2)
        self.assertTrue(all(not p.is_symlink() for p in self.links()))


if __name__ == '__main__':
    unittest.main()
