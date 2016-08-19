from __future__ import absolute_import, print_function
from getkey.keys import PLATFORM_KEYS


PLATFORM_CHARS = [
    ('unix', 'u'),
    ('windows', 'w'),
]


CANON = '*'


def main():
    names = set()
    for platform in PLATFORM_KEYS.values():
        names.update(platform.names)

    items = list()
    for name in sorted(names):
        v = ''
        for platform, char in PLATFORM_CHARS:
            keys = PLATFORM_KEYS[platform]
            code = keys.code(name)
            if code:
                v += char
            else:
                v += ' '
            if code and name == keys.name(code):
                v += CANON
            else:
                v += ' '
        v += ' ' + name
        items.append(v)
    print('\n'.join(items))


if __name__ == '__main__':
    main()
