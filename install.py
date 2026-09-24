#!/usr/bin/env python3
"""Opt-in, single-owner skill links. Python 3.10+, Git, macOS/Linux."""
import argparse
import contextlib
import fcntl
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def present(path):
    return path.exists() or path.is_symlink()


def same_link(path, target):
    return path.is_symlink() and Path(os.path.abspath(path.parent / os.readlink(path))) == target


def no_symlink_parents(path):
    for parent in [path, *path.parents]:
        if parent.is_symlink():
            raise ValueError(f'Symlinked destination directory: {parent}; select its real path explicitly')


def verify_source(path, source):
    if path.is_symlink():
        raise ValueError(f'Source checkout must use its real path: {path}')
    if git(path, 'rev-parse', 'HEAD') != source['revision']:
        raise ValueError(f'Source revision differs from manifest: {path}')
    if git(path, 'status', '--porcelain', '--untracked-files=all'):
        raise ValueError(f'Source has local changes: {path}; preserve them and resolve manually')


def fetch_source(path, source):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Build beside the destination. Failed downloads never become canonical sources.
    with tempfile.TemporaryDirectory(prefix='.fetch-', dir=path.parent) as temporary:
        checkout = Path(temporary) / 'checkout'
        subprocess.run(['git', 'clone', '--no-checkout', source['url'], str(checkout)], check=True)
        subprocess.run(['git', '-C', str(checkout), '-c', 'core.hooksPath=/dev/null',
                        'checkout', '--detach', source['revision']], check=True)
        verify_source(checkout, source)
        if present(path):
            raise ValueError(f'Source appeared during fetch: {path}')
        checkout.rename(path)


def write_state(path, state):
    with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(state, stream, indent=2)
        stream.write('\n')
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def run(args):
    manifest = json.loads((ROOT / 'sources.json').read_text())
    if args.list:
        for name, entry in manifest['skills'].items():
            print(f'{name:26} owner={entry["owner"]}')
        return 0
    names = args.skills or manifest['profiles'][args.profile]
    if len(names) != len(set(names)):
        raise ValueError('Select each skill once')
    for name in names:
        if name not in manifest['skills'] or not re.fullmatch(r'[a-z0-9-]+', name):
            raise ValueError(f'Unknown skill: {name}; use --list')
    home = Path(args.home).expanduser().resolve()
    targets = {
        'claude': Path(args.claude_dir).expanduser().absolute() if args.claude_dir else home / '.claude/skills',
        'codex': Path(args.codex_dir).expanduser().absolute() if args.codex_dir else home / '.agents/skills',
    }
    harnesses = list(dict.fromkeys(args.harness))
    roots = [targets[h] for h in harnesses]
    if len(set(roots)) != len(roots):
        raise ValueError('Harness destinations must be distinct')
    for root in roots:
        no_symlink_parents(root)
    overrides = {}
    for value in args.source:
        owner, separator, location = value.partition('=')
        if not separator or owner not in manifest['sources'] or owner in overrides:
            raise ValueError('--source requires a unique known OWNER=/absolute/checkout')
        overrides[owner] = Path(location).expanduser().absolute()
    state_dir = ROOT / '.state'
    state_file = state_dir / 'links.json'
    if args.apply:
        state_dir.mkdir(exist_ok=True)
    # One writer per installation. Read-only modes never create files or use network.
    with contextlib.ExitStack() as stack:
        if args.apply:
            lock = stack.enter_context((state_dir / 'lock').open('a'))
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        receipt = json.loads(state_file.read_text()) if state_file.exists() else {'links': {}, 'sources': {}}
        state = receipt['links']
        bindings = dict(receipt['sources'])
        for owner, location in overrides.items():
            if owner in bindings and bindings[owner] != str(location):
                raise ValueError(f'Source already bound to {bindings[owner]}; use that canonical owner')
        overrides = {**{k: Path(v) for k, v in bindings.items()}, **overrides}
        actions, missing_sources, source_paths = [], {}, {}
        needed = set()
        for name in names:
            entry = manifest['skills'][name]
            needed.update(entry.get('requires', []))
            if entry['owner'] != 'shared-agent-harness':
                needed.add(entry['owner'])
        for owner in sorted(needed):
            source = manifest['sources'][owner]
            source_root = overrides.get(owner, ROOT / '.sources' / owner / source['revision'])
            source_paths[owner] = source_root
            if not args.uninstall:
                if present(source_root):
                    verify_source(source_root, source)
                elif owner in overrides:
                    raise ValueError(f'Explicit source does not exist: {source_root}')
                else:
                    missing_sources[owner] = (source_root, source)
        for name in names:
            entry = manifest['skills'][name]
            owner = entry['owner']
            if owner == 'shared-agent-harness':
                source_root = ROOT
            else:
                source_root = source_paths[owner]
            source_path = source_root / entry['path']
            if not args.uninstall and owner not in missing_sources:
                if not source_path.resolve().is_relative_to(source_root.resolve()):
                    raise ValueError(f'Skill escapes source owner: {name}')
                if not (source_path / 'SKILL.md').is_file():
                    raise ValueError(f'SKILL.md missing: {source_path}')
            for harness in harnesses:
                destination = targets[harness] / name
                key = str(destination)
                owned = state.get(key)
                if args.uninstall:
                    if owned:
                        if owned['owner'] != owner:
                            raise ValueError(f'Owner changed: {destination}')
                        old_target = Path(owned['target'])
                        if present(destination) and not same_link(destination, old_target):
                            raise ValueError(f'Owned link was replaced; leaving it intact: {destination}')
                        actions.append(('remove', destination, old_target, owner))
                    continue
                # Avoid duplicate discovery in Codex's older personal loader.
                if harness == 'codex':
                    legacy = home / '.codex/skills' / name
                    if legacy != destination and present(legacy):
                        raise ValueError(f'Existing legacy Codex skill: {legacy}; use its current owner')
                if owned:
                    if owned['owner'] != owner:
                        raise ValueError(f'Owner changed: {destination}')
                    old_target = Path(owned['target'])
                    if present(destination) and not same_link(destination, old_target):
                        raise ValueError(f'Owned link was replaced; leaving it intact: {destination}')
                elif present(destination):
                    raise ValueError(f'Unowned destination exists: {destination}; no overwrite or adoption')
                if not same_link(destination, source_path):
                    actions.append(('link', destination, source_path, owner))
        if not args.uninstall:
            selected_destinations = {str(targets[h] / n) for h in harnesses for n in names}
            for destination, owned in state.items():
                owner = owned['owner']
                if owner not in source_paths:
                    continue
                name = Path(destination).name
                entry = manifest['skills'].get(name)
                if not entry or entry['owner'] != owner:
                    raise ValueError(f'Installed skill lost its manifest owner: {name}')
                expected = source_paths[owner] / entry['path']
                if owned['target'] != str(expected) and destination not in selected_destinations:
                    raise ValueError(f'Source update would leave an old projection: {destination}; '
                                     'include every installed skill and harness for this owner')
        for owner, (_, source) in missing_sources.items():
            print(f'FETCH {owner} {source["url"]} @ {source["revision"]}')
        for action, destination, source_path, _ in actions:
            print(f'{action.upper()} {destination} -> {source_path}')
        print(f'Planned: {len(missing_sources)} source fetches, {len(actions)} link changes')
        if not args.apply:
            return 1 if args.check and (actions or missing_sources) else 0
        for path, source in missing_sources.values():
            fetch_source(path, source)
        # Validate downloaded contents before changing any loader.
        for action, _, target, _ in actions:
            if action == 'link' and not (target / 'SKILL.md').is_file():
                raise ValueError(f'SKILL.md missing: {target}')
        previous, new_state = [], dict(state)
        try:
            for action, destination, target, owner in actions:
                no_symlink_parents(destination.parent)
                key = str(destination)
                old = state.get(key)
                if present(destination):
                    if not old or not same_link(destination, Path(old['target'])):
                        raise ValueError(f'Destination changed after preview: {destination}')
                    previous.append((destination, os.readlink(destination)))
                    destination.unlink()
                else:
                    previous.append((destination, None))
                if action == 'link':
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.symlink_to(target, target_is_directory=True)
                    new_state[key] = {'owner': owner, 'target': str(target)}
                else:
                    new_state.pop(key, None)
            write_state(state_file, {'links': new_state, 'sources': {k: str(v) for k, v in overrides.items()}})
        except Exception:
            for destination, old_target in reversed(previous):
                if destination.is_symlink():
                    destination.unlink()
                if old_target is not None and not present(destination):
                    destination.symlink_to(old_target, target_is_directory=True)
            raise
        print('Applied. Run the same selection with --check, then verify discovery in fresh harness sessions.')
        return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--apply', action='store_true', help='apply the printed plan')
    modes.add_argument('--check', action='store_true', help='read-only; exit 1 if work remains')
    parser.add_argument('--uninstall', action='store_true', help='remove selected owned links; keep sources')
    parser.add_argument('--list', action='store_true', help='list installer-supported skills')
    parser.add_argument('--profile', choices=['minimal', 'core', 'curated'], default='minimal')
    parser.add_argument('--skills', nargs='+', help='default: cmux-orchestrate')
    parser.add_argument('--harness', nargs='+', choices=['claude', 'codex'], default=['claude', 'codex'])
    parser.add_argument('--home', default=str(Path.home()), help='alternate home for isolated testing')
    parser.add_argument('--claude-dir', help='explicit Claude skill loader')
    parser.add_argument('--codex-dir', help='explicit Codex skill loader')
    parser.add_argument('--source', action='append', default=[], help='reuse OWNER=/existing/pinned/checkout')
    try:
        return run(parser.parse_args())
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
