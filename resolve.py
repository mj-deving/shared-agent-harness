#!/usr/bin/env python3
"""Resolve one admitted vendor leaf; never execute it or fetch dependencies."""
import argparse
import json
from pathlib import Path
import sys
from install import ROOT, verify_source


def resolve(owner, name):
    manifest = json.loads((ROOT / 'sources.json').read_text())
    catalog = manifest['catalog'].get(owner, {})
    if name not in catalog:
        raise ValueError(f'Unknown {owner} leaf {name}; choose from: {", ".join(catalog)}')
    receipt = ROOT / '.state/links.json'
    bindings = json.loads(receipt.read_text())['sources'] if receipt.exists() else {}
    source = manifest['sources'][owner]
    root = Path(bindings.get(owner, ROOT / '.sources' / owner / source['revision']))
    verify_source(root, source)
    leaf = root / catalog[name] / 'SKILL.md'
    if not leaf.resolve().is_relative_to(root.resolve()) or not leaf.is_file():
        raise ValueError(f'Missing or escaping canonical leaf: {name}')
    result = {'owner': owner, 'revision': source['revision'], 'skill': name,
              'path': str(leaf), 'source_root': str(root)}
    if owner == 'lifeos' and name == 'CMUX':
        script = leaf.parent / 'Tools/cmux.ts'
        if not script.is_file() or not script.resolve().is_relative_to(root.resolve()):
            raise ValueError('Missing or escaping canonical CMUX script')
        result['script'] = str(script)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('owner', choices=['lifeos', 'agent-scripts'])
    parser.add_argument('name')
    args = parser.parse_args()
    try:
        print(json.dumps(resolve(args.owner, args.name), indent=2))
    except Exception as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(2)
