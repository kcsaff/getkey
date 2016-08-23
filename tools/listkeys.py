# List all key names & canonical codes for different systems
# Generates `keys.txt` and `controls.txt`

from __future__ import absolute_import, print_function
import argparse
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from getkey.keynames import PLATFORM_KEYS


PLATFORM_CHARS = [
    ('unix', 'u'),
    ('windows', 'w'),
]


CANON = '*'


PREAMBLE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'listpreamble.txt')
)


def main(accept=None):
    names = set()
    for platform in PLATFORM_KEYS.values():
        names.update(platform.names)

    items = list()
    max_name_len = max(len(name) for name in names)
    for name in sorted(names):
        v = ''
        codes = []
        for platform, char in PLATFORM_CHARS:
            keys = PLATFORM_KEYS[platform]
            code = keys.code(name)

            if code:
                codes.append(code)
                v += char
            else:
                v += ' '
            if code and name == keys.name(code):
                v += CANON
            else:
                v += ' '

        if accept and not accept(name, codes):
            continue

        v += ' ' + name
        v += ' ' * (2 + max_name_len - len(name))

        if len(set(codes)) == 1:
            v += repr(codes[0])
        else:
            v += ', '.join(
                '{}{!r}'.format(char, code)
                for code, (_, char) in zip(codes, PLATFORM_CHARS)
                if code
            )

        items.append(v)
    print('\n'.join(items))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='List all defined key names & canonical codes'
    )
    parser.add_argument('--controls', '-c', action='store_true',
                        help='Only list control keys')
    args = parser.parse_args()

    preamble = open(PREAMBLE_PATH).read().format(
        'control' if args.controls else 'all'
    )

    def accept_controls(name, codes):
        return 'CTRL_' in name or 'ALT_' in name or \
            all(len(code) >= 2 for code in codes)

    print(preamble)
    main(accept_controls if args.controls else None)
