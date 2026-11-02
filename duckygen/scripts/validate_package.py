#!/usr/bin/env python3
"""Check portable package links, Python syntax, and pinned companion integrity."""

import ast
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    documents = [ROOT / 'SKILL.md', ROOT / 'README.md', ROOT / 'example-prompt.md',
                 ROOT / 'THIRD_PARTY_NOTICES.md', *sorted((ROOT / 'references').glob('*.md'))]
    for document in documents:
        if not document.is_file():
            errors.append(f'Missing document: {document.relative_to(ROOT)}')
            continue
        # Only check maintained package guidance; upstream documents retain their
        # original links and may describe files outside the bundled subset.
        for target in re.findall(r'\]\(([^)\s]+)\)', document.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            if not (document.parent / unquote(url.path)).exists():
                errors.append(f'Broken link in {document.relative_to(ROOT)}: {target}')

    for script in sorted((ROOT / 'scripts').glob('*.py')):
        try:
            ast.parse(script.read_text(), filename=str(script))
        except SyntaxError as error:
            errors.append(f'Python syntax: {script.name}: {error}')

    checked = 0

    def check_file(base, relative, expected):
        nonlocal checked
        path = (base / relative).resolve()
        if not path.is_relative_to(base.resolve()) or not path.is_file():
            errors.append(f'Missing/unsafe companion file: {relative}')
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append(f'Companion hash differs: {path.relative_to(ROOT)}')
        checked += 1

    companions = ROOT / 'companions'
    for name in ['remotion-best-practices', 'lemo-opuscar']:
        base = companions / name
        manifest = json.loads((base / 'upstream.json').read_text())
        for relative, expected in manifest['files'].items():
            check_file(base, relative, expected)
    manifest = json.loads((companions / 'hyperframes-provenance.json').read_text())
    for item in manifest['files']:
        check_file(companions, item['path'], item['sha256'])

    print(json.dumps({'valid': not errors, 'documents': len(documents),
                      'companion_files': checked, 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
