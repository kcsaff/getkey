# Which key(s) were pressed
# What chars to print (if any)
# Keycode(s) generating event
import string


ASCII_NAMES = {
    '\t': 'tab',

    ' ': 'space',                # 0x20
    '!': 'exclamation',          # 0x21
    '"': 'double quote',         # 0x22
    '#': 'hash',                 # 0x23
    '$': 'dollar',               # 0x24
    '%': 'percent',              # 0x25
    '&': 'ampersand',            # 0x26
    '\'': 'single quote',        # 0x27
    '(': 'open paren',           # 0x28
    ')': 'close paren',          # 0x29
    '*': 'asterisk',             # 0x2a
    '+': 'plus',                 # 0x2b
    ',': 'comma',                # 0x2c
    '-': 'minus',                # 0x2d
    '.': 'period',               # 0x2e
    '/': 'slash',                # 0x2f

    ':': 'colon',                # 0x3a
    ';': 'semicolon',            # 0x3b
    '<': 'less than',            # 0x3c
    '=': 'equals',               # 0x3d
    '>': 'greater than',         # 0x3e
    '?': 'question',             # 0x3f
    '@': 'at',                   # 0x40

    '[': 'left bracket',         # 0x5b
    '\\': 'backslash',           # 0x5c
    ']': 'right bracket',        # 0x5d
    '^': 'caret',                # 0x5e
    '_': 'underscore',           # 0x5f
    '`': 'backtick',             # 0x60

    '{': 'left curly bracket',   # 0x7b
    '|': 'pipe',                 # 0x7c
    '}': 'right curly bracket',  # 0x7d
    '~': 'tilde',                # 0x7e
}


class UnixKeys(object):

    ESC = '\x1b'

    UP = '\x1b[A'
    DOWN = '\x1b[B'
    RIGHT = '\x1b[C'
    LEFT = '\x1b[D'
    ENTER = '\n'
    CR = '\r'
    BACKSPACE = '\x7f'

    SPACE = ' '

    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'
    F5 = '\x1b\x4f15~'
    F6 = '\x1b\x4f17~'
    F7 = '\x1b\x4f18~'
    F8 = '\x1b\x4f19~'
    F9 = '\x1b\x4f20~'
    F10 = '\x1b\x4f21~'
    F11 = '\x1b\x4f23~'
    F12 = '\x1b\x4f24~'

    INSERT = '\x1b[2~'
    DELETE = '\x1b[3~'
    HOME = '\x1b[H'
    END = '\x1b[F'
    PAGE_UP = '\x1b[5'
    PAGE_DOWN = '\x1b[6'


class UnixControlKeys(object):
    def __init__(self, format='CTRL_{}'):
        for i in range(0x20):
            low_char = chr(i)
            high_char = chr(i + 0x40)
            name = ASCII_NAMES.get(high_char, high_char).upper()
            ctrl_name = format.format(name)
            setattr(self, ctrl_name, low_char)


class AsciiKeys(object):
    def __init__(
            self,
            lower_format='{}', upper_format='SHIFT_{}', digit_format='N{}',
            ascii_names=ASCII_NAMES,
    ):
        for letter in string.ascii_lowercase:
            name = lower_format.format(letter.upper())
            setattr(self, name, letter)
        for letter in string.ascii_uppercase:
            name = upper_format.format(letter.upper())
            setattr(self, name, letter)
        for digit in string.digits:
            name = digit_format.format(digit)
            setattr(self, name, digit)
        for char, name in ascii_names.items():
            name = name.upper().replace(' ', '_')
            setattr(self, name, char)


class Keys(object):
    def __init__(self, keyclasses):
        self.__names = dict()  # Map of codes -> names
        self.__codes = dict()  # Map of names -> codes (can be updated towards canonicity)

        self.__escapes = set()

        for keyclass in keyclasses:
            for name in dir(keyclass):
                if self._is_key_name(name):
                    code = getattr(keyclass, name)
                    self.register(name, code)

    def register(self, name, code):
        if name not in self.__codes:
            self.__codes[name] = code
        if code not in self.__names:
            self.__names[code] = name
        for i in range(len(code)):
            self.__escapes.add(code[:i])

        # Update towards canonicity
        while True:
            canon_code = self.canon(code)
            canon_canon_code = self.canon(canon_code)
            if canon_code != canon_canon_code:
                self.__codes[self.name(code)] = canon_canon_code
            else:
                break
        while True:
            canon_name = self.name(self.code(name))
            canon_canon_name = self.name(self.code(canon_name))
            if canon_name != canon_canon_name:
                self.__names[self.code(name)] = canon_canon_name
            else:
                break

    @property
    def escapes(self):
        return self.__escapes

    @property
    def names(self):
        return self.__codes.keys()

    def name(self, code):
        return self.__names.get(code)

    def code(self, name):
        return self.__codes.get(name)

    def canon(self, code):
        name = self.name(code)
        return self.code(name) if name else code

    def __getattr__(self, name):
        code = self.code(name)
        if code is not None:
            return code
        else:
            return self.__getattribute__(name)

    def _is_key_name(self, name):
        return name == name.upper() and not name.startswith('_')


def _make_escapes(codes):
    escapes = set()
    for code in codes:
        for i in range(len(code)):
            escapes.add(code[:i])
    return escapes


unix_keys = Keys([UnixKeys(), AsciiKeys(), UnixControlKeys()])
windows_keys = unix_keys  # This is wrong, rite?


PLATFORM_KEYS = {
    'unix': unix_keys,
    'windows': windows_keys,
}


# ALT
ALT_A = '\x1b\x61'

# CTRL + ALT
CTRL_ALT_A = '\x1b\x01'

CTRL_ALT_SUPR = '\x1b\x5b\x33\x5e'



