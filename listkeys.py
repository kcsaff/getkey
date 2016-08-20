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
    max_name_len = max(len(name) for name in names)
    for name in sorted(names):
        v = ''
        codes = []
        for platform, char in PLATFORM_CHARS:
            keys = PLATFORM_KEYS[platform]
            code = keys.code(name)
            codes.append(code)
            if code:
                v += char
            else:
                v += ' '
            if code and name == keys.name(code):
                v += CANON
            else:
                v += ' '
        v += ' ' + name
        v += ' ' * (2 + max_name_len - len(name))

        if len(set(codes)) == 1:
            v += repr(codes[0])
        else:
            v += ', '.join('{}{!r}'.format(char, code)
                           for code, (_, char) in zip(codes, PLATFORM_CHARS)
			   if code
			   )

        items.append(v)
    print('\n'.join(items))


if __name__ == '__main__':
    main()
