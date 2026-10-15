"""Read exact Markdown sections and their ancestor scope; standard library only."""
import argparse
import json
from pathlib import Path
import re
import sys


def headings(text):
    lines = text.splitlines(keepends=True)
    result = []
    fence = None
    for position, line in enumerate(lines):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[marker.end():].strip():
                fence = None
            continue
        if fence:
            continue
        match = re.match(r'^ {0,3}(#{1,6})\s+(.+?)\s*$', line)
        if match:
            result.append({'title': re.sub(r'\s+#+\s*$', '', match.group(2)),
                           'level': len(match.group(1)), 'start': position})
    ancestry = []
    for offset, item in enumerate(result):
        while ancestry and ancestry[-1]['level'] >= item['level']:
            ancestry.pop()
        item['path'] = ' > '.join(parent['title'] for parent in ancestry + [item])
        ancestry.append(item)
        item['end'] = next((other['start'] for other in result[offset + 1:]
                            if other['level'] <= item['level']), len(lines))
        item['preamble_end'] = result[offset + 1]['start'] if offset + 1 < len(result) else len(lines)
    return result


def extract(text, names):
    lines = text.splitlines(keepends=True)
    index = headings(text)
    selected = set()
    for name in names:
        matches = [item for item in index if item['title'] == name or item['path'] == name]
        if len(matches) != 1:
            raise ValueError(f'Section must match exactly once: {name!r} ({len(matches)} matches)')
        item = matches[0]
        selected.update(range(item['start'], item['end']))
        # Ancestor introductory prose contains scope/precedence, not sibling rules.
        for parent in index:
            if parent['start'] < item['start'] < parent['end'] and parent['level'] < item['level']:
                selected.update(range(parent['start'], parent['preamble_end']))
        if index and index[0]['start'] > 0:
            selected.update(range(index[0]['start']))
    return ''.join(lines[position] for position in sorted(selected))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', help='Markdown path relative to the skill root')
    parser.add_argument('--list', action='store_true', help='List exact heading names and line spans')
    parser.add_argument('--find', help='Filter the heading list by a case-insensitive title substring')
    parser.add_argument('--section', action='append', default=[], help='Exact heading; repeat to select more')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    file = (root / args.file).resolve()
    try:
        file.relative_to(root)
        if file.suffix.lower() != '.md':
            raise ValueError('Only Markdown resources are supported')
        text = file.read_text(encoding='utf-8-sig')
        if args.find and not args.list:
            raise ValueError('--find requires --list')
        if args.list:
            index = headings(text)
            if args.find:
                index = [item for item in index if args.find.casefold() in item['title'].casefold()]
            output = json.dumps([{'heading': item['title'], 'path': item['path'], 'level': item['level'],
                                  'first_line': item['start'] + 1, 'last_line': item['end']}
                                 for item in index], ensure_ascii=False, indent=2)
        elif args.section:
            output = extract(text, args.section)
        else:
            raise ValueError('Choose --list or at least one --section; no implicit whole-file read')
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 2
    sys.stdout.buffer.write(output.encode('utf-8'))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
