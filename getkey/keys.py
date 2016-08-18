# Which key(s) were pressed
# What chars to print (if any)
# Keycode(s) generating event
import string


ASCII_NAMES = {
    ' ': 'space',                # 0x20
    '!': 'exclamation',          # 0x21
    '"': 'double quote',         # 0x22
    '#': 'hash',                 # 0x23
    '$': 'dollar',               # 0x24

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
    UP = '\x1b[A'
    DOWN = '\x1b[B'
    RIGHT = '\x1b[C'
    LEFT = '\x1b[D'
    ENTER = '\n'
    CR = '\r'
    BACKSPACE = '\x7f'
    DELETE = '\x1b[3~'

    SPACE = ' '

    F1 = '\x1b\x4f\x50'
    F2 = '\x1b\x4f\x51'
    F3 = '\x1b\x4f\x52'
    F4 = '\x1b\x4f\x53'
    F5 = '\x1b\x4f\x31\x35~'
    F6 = '\x1b\x4f\x31\x37~'
    F7 = '\x1b\x4f\x31\x38~'
    F8 = '\x1b\x4f\x31\x39~'
    F9 = '\x1b\x4f\x32\x30~'
    F10 = '\x1b\x4f\x32\x31~'
    F11 = '\x1b\x4f\x32\x33~'
    F12 = '\x1b\x4f\x32\x34~'

    ESC = '\x1b'

    INSERT = '\x1b[2~'
    SUPR = '\x1b[3~'


class UnixControlKeys(object):
    def __init__(self, format='CTRL_{}'):
        for i in range(0x20):
            low_char = chr(i)
            high_char = chr(i + 0x40)
            name = ASCII_NAMES.get(high_char, high_char).upper()
            ctrl_name = format.format(name)
            setattr(ctrl_name, low_char)


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
            self.__escapes.update(code[:i])

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

    def escapes(self):
        return self.__escapes

    def name(self, code):
        return self.__names.get(code)

    def code(self, name):
        return self.__codes.get(name)

    def canon(self, code):
        return self.code(self.name(code))

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


unix = Keys([UnixKeys(), UnixControlKeys(), AsciiKeys()])
windows = unix  # This is wrong, rite?


# ALT
ALT_A = '\x1b\x61'

# CTRL + ALT
CTRL_ALT_A = '\x1b\x01'

CTRL_ALT_SUPR = '\x1b\x5b\x33\x5e'



