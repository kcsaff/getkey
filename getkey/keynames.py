# Which key(s) were pressed
# What chars to print (if any)
# Keycode(s) generating event
import string
from .unikeys import UnicodeAsciiKeys


# These are used for the names of ctrl keys, etc.
ASCII_NAMES = {
    '\t': 'tab',

    ' ': 'space',          # 0x20
    '!': 'exclamation',    # 0x21
    '"': 'double quote',   # 0x22
    '#': 'hash',           # 0x23
    '$': 'dollar',         # 0x24
    '%': 'percent',        # 0x25
    '&': 'ampersand',      # 0x26
    '\'': 'single quote',  # 0x27
    '(': 'open paren',     # 0x28
    ')': 'close paren',    # 0x29
    '*': 'asterisk',       # 0x2a
    '+': 'plus',           # 0x2b
    ',': 'comma',          # 0x2c
    '-': 'minus',          # 0x2d
    '.': 'period',         # 0x2e
    '/': 'slash',          # 0x2f

    ':': 'colon',          # 0x3a
    ';': 'semicolon',      # 0x3b
    '<': 'less than',      # 0x3c
    '=': 'equals',         # 0x3d
    '>': 'greater than',   # 0x3e
    '?': 'question',       # 0x3f
    '@': 'at',             # 0x40

    '[': 'left bracket',   # 0x5b
    '\\': 'backslash',     # 0x5c
    ']': 'right bracket',  # 0x5d
    '^': 'caret',          # 0x5e
    '_': 'underscore',     # 0x5f
    '`': 'backtick',       # 0x60

    '{': 'left brace',     # 0x7b
    '|': 'pipe',           # 0x7c
    '}': 'right brace',    # 0x7d
    '~': 'tilde',          # 0x7e
}


class UnicodeKeys(object):
    # Names from ftp://ftp.unicode.org/Public/UNIDATA/NamesList.txt
    NULL = chr(0x00)
    START_OF_HEADING = chr(0x01)


class JargonKeys(object):
    BANG = '!'
    SHRIEK = '!'
    DOUBLE_QUOTE = '"'
    QUOTE = '"'
    NUMBER_SIGN = '#'
    SHARP = '#'
    OCTOTHORPE = '#'
    BUCK = '$'
    CASH = '$'
    STRING = '$'
    MOD = '%'
    GRAPES = '%'
    AMPERSAND = '&'
    AMP = '&'
    AND_SIGN = '&'
    APOSTROPHE = '\''
    PRIME = '\''
    TICK = '\''
    STAR = '*'
    SPLAT = '*'
    GLOB = '*'
    ADD = '+'


class IntercalKeys(object):
    SPOT = '.'
    TWO_SPOT = ':'
    TAIL = ','
    HYBRID = ';'
    MESH = '#'
    HALF_MESH = '='
    SPARK = '\''
    BACKSPARK = '`'
    WOW = '!'
    WHAT = '?'
    RABBIT_EARS = '"'
    # RABBIT is `"` over `.`
    SPIKE = '|'
    DOUBLE_OH_SEVEN = '%'
    WORM = '-'
    ANGLE = '<'
    RIGHT_ANGLE = '>'
    WAX = '('
    WANE = ')'
    U_TURN = '['
    U_TURN_BACK = ']'
    EMBRACE = '{'
    BRACELET = '}'
    SPLAT = '*'
    AMPERSAND = '&'
    V = 'V'
    BOOK = 'V'
    # BOOKWORM is `-` over `V`
    BIG_MONEY = '$'
    # CHANGE is cent sign
    SQUIGGLE = '~'
    FLAT_WORM = '_'
    # OVERLINE is line on top
    INTERSECTION = '+'
    SLAT = '/'
    BACKSLAT = '\\'
    WHIRLPOOL = '@'
    # HOOKWORK is logical NOT symbol
    SHARK = '^'
    SHARKFIN = '^'
    # BLOTCH is several characters smashed on top of each other


class VT100StandardModeKeys(object):
    # http://www.braun-home.net/michael/mbedit/info/misc/VT100_commands.htm
    # http://www.ccs.neu.edu/research/gpc/MSim/vona/terminal/VT100_Escape_Codes.html
    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'

    UP = '\x1b[A'
    DOWN = '\x1b[B'
    RIGHT = '\x1b[C'
    LEFT = '\x1b[D'


class VT100ApplicationsModeKeys(object):
    F1 = '\x1bOP'
    F2 = '\x1bOQ'
    F3 = '\x1bOR'
    F4 = '\x1bOS'

    UP = '\x1bOA'
    DOWN = '\x1bOB'
    RIGHT = '\x1bOC'
    LEFT = '\x1bOD'

    KEYPAD_0 = '\x1bOp'
    KEYPAD_1 = '\x1bOq'
    KEYPAD_2 = '\x1bOr'
    KEYPAD_3 = '\x1bOs'
    KEYPAD_4 = '\x1bOt'
    KEYPAD_5 = '\x1bOu'
    KEYPAD_6 = '\x1bOv'
    KEYPAD_7 = '\x1bOw'
    KEYPAD_8 = '\x1bOx'
    KEYPAD_9 = '\x1bOy'
    KEYPAD_MINUS = '\x1bOm'
    KEYPAD_COMMA = '\x1bOl'
    KEYPAD_PERIOD = '\x1bOn'
    KEYPAD_ENTER = '\x1bOM'


class VT220Keys(object):
    # F1-F5 didn't exist historically, but were added by later emulators
    F1 = '\x1b[11~'
    F2 = '\x1b[12~'
    F3 = '\x1b[13~'
    F4 = '\x1b[14~'
    F5 = '\x1b[15~'

    # Historical keys
    F6 = '\x1b[17~'
    F7 = '\x1b[18~'
    F8 = '\x1b[19~'
    F9 = '\x1b[20~'
    F10 = '\x1b[21~'
    F11 = '\x1b[23~'
    F12 = '\x1b[24~'

    # F13+ and key combinations to enter them are of limited usefulness today


class UnixKeys(object):
    # Keys found experimentally, of unknown provenance
    ESC = '\x1b'

    HOME = '\x1b[H'
    END = '\x1b[F'
    PAGE_UP = '\x1b[5'
    PAGE_DOWN = '\x1b[6'

    ENTER = '\n'
    CR = '\r'
    BACKSPACE = '\x7f'

    SPACE = ' '

    INSERT = '\x1b[2~'
    DELETE = '\x1b[3~'


class AlternativeUnixFunctionKeys(object):
    # Unsure origin: alternate V220 mode?
    F1 = '\x1bO11~'
    F2 = '\x1bO12~'
    F3 = '\x1bO13~'
    F4 = '\x1bO14~'
    F5 = '\x1bO15~'
    F6 = '\x1bO17~'
    F7 = '\x1bO18~'
    F8 = '\x1bO19~'
    F9 = '\x1bO20~'
    F10 = '\x1bO21~'
    F11 = '\x1bO23~'
    F12 = '\x1bO24~'


class WindowsKeys(object):
    ESC = '\x1b'

    LEFT = '\xe0K'
    RIGHT = '\xe0M'
    UP = '\xe0H'
    DOWN = '\xe0P'
    
    ENTER = '\r'
    BACKSPACE = '\x08'
    SPACE = ' '

    F1 = '\x00;'
    F2 = '\x00<'
    F3 = '\x00='
    F4 = '\x00>'
    F5 = '\x00?'
    F6 = '\x00@'
    F7 = '\x00A'
    F8 = '\x00B'
    F9 = '\x00C'
    F10 = '\x00D'
    F11 = '\xe0\x85'
    F12 = '\xe0\x86'

    INSERT = '\xe0R'
    DELETE = '\xe0S'
    PAGE_UP = '\xe0I'
    PAGE_DOWN = '\xe0Q'
    HOME = '\xe0G'
    END = '\xe0O'

    CTRL_F1 = '\x00^'
    CTRL_F2 = '\x00_'
    CTRL_F3 = '\x00`'
    CTRL_F4 = '\x00a'
    CTRL_F5 = '\x00b'
    CTRL_F6 = '\x00c'
    CTRL_F7 = '\x00d'  # Captured by something?
    CTRL_F8 = '\x00e'
    CTRL_F9 = '\x00f'
    CTRL_F10 = '\x00g'
    CTRL_F11 = '\xe0\x89'
    CTRL_F12 = '\xe0\x8a'

    CTRL_HOME = '\xe0w'
    CTRL_END = '\xe0u'
    CTRL_INSERT = '\xe0\x92'
    CTRL_DELETE = '\xe0\x93'
    CTRL_PAGE_DOWN = '\xe0v'

    CTRL_2 = '\x00\x03'
    CTRL_UP = '\xe0\x8d'
    CTRL_DOWN = '\xe0\x91'
    CTRL_LEFT = '\xe0s'
    CTRL_RIGHT = '\xe0t'

    CTRL_ALT_A = '\x00\x1e'
    CTRL_ALT_B = '\x000'
    CTRL_ALT_C = '\x00.'
    CTRL_ALT_D = '\x00 '
    CTRL_ALT_E = '\x00\x12'
    CTRL_ALT_F = '\x00!'
    CTRL_ALT_G = '\x00"'
    CTRL_ALT_H = '\x00#'
    CTRL_ALT_I = '\x00\x17'
    CTRL_ALT_J = '\x00$'
    CTRL_ALT_K = '\x00%'
    CTRL_ALT_L = '\x00&'
    CTRL_ALT_M = '\x002'
    CTRL_ALT_N = '\x001'
    CTRL_ALT_O = '\x00\x18'
    CTRL_ALT_P = '\x00\x19'
    CTRL_ALT_Q = '\x00\x10'
    CTRL_ALT_R = '\x00\x13'
    CTRL_ALT_S = '\x00\x1f'
    CTRL_ALT_T = '\x00\x14'
    CTRL_ALT_U = '\x00\x16'
    CTRL_ALT_V = '\x00/'
    CTRL_ALT_W = '\x00\x11'
    CTRL_ALT_X = '\x00-'
    CTRL_ALT_Y = '\x00\x15'
    CTRL_ALT_Z = '\x00,'
    CTRL_ALT_1 = '\x00x'
    CTRL_ALT_2 = '\x00y'
    CTRL_ALT_3 = '\x00z'
    CTRL_ALT_4 = '\x00{'
    CTRL_ALT_5 = '\x00|'
    CTRL_ALT_6 = '\x00}'
    CTRL_ALT_7 = '\x00~'
    CTRL_ALT_8 = '\x00\x7f'
    CTRL_ALT_9 = '\x00\x80'
    CTRL_ALT_0 = '\x00\x81'
    CTRL_ALT_MINUS = '\x00\x82'
    CTRL_ALT_EQUALS = '\x00x83'
    CTRL_ALT_BACKSPACE = '\x00\x0e'

    ALT_F1 = '\x00h'
    ALT_F2 = '\x00i'
    ALT_F3 = '\x00j'
    ALT_F4 = '\x00k'
    ALT_F5 = '\x00l'
    ALT_F6 = '\x00m'
    ALT_F7 = '\x00n'
    ALT_F8 = '\x00o'
    ALT_F9 = '\x00p'
    ALT_F10 = '\x00q'
    ALT_F11 = '\xe0\x8b'
    ALT_F12 = '\xe0\x8c'
    ALT_HOME = '\x00\x97'
    ALT_END = '\x00\x9f'
    ALT_INSERT = '\x00\xa2'
    ALT_DELETE = '\x00\xa3'
    ALT_PAGE_UP = '\x00\x99'
    ALT_PAGE_DOWN = '\x00\xa1'
    ALT_LEFT = '\x00\x9b'
    ALT_RIGHT = '\x00\x9d'
    ALT_UP = '\x00\x98'
    ALT_DOWN = '\x00\xa0'

    CTRL_ALT_LEFT_BRACKET = '\x00\x1a'
    CTRL_ALT_RIGHT_BRACKET = '\x00\x1b'
    CTRL_ALT_SEMICOLON = '\x00\''
    CTRL_ALT_SINGLE_QUOTE = '\x00('
    CTRL_ALT_ENTER = '\x00\x1c'
    CTRL_ALT_SLASH = '\x005'
    CTRL_ALT_PERIOD = '\x004'
    CTRL_ALT_COMMA = '\x003'


class ControlKeys(object):
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
        self.__codes = dict()  # Map of names -> codes

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


unix_keys = Keys([
    VT100StandardModeKeys(),
    VT100ApplicationsModeKeys(),
    VT220Keys(),
    UnixKeys(),
    AlternativeUnixFunctionKeys(),
    AsciiKeys(),
    ControlKeys(),
    UnicodeAsciiKeys(),
    JargonKeys(),
    IntercalKeys()
])
windows_keys = Keys([
    WindowsKeys(),
    AsciiKeys(),
    ControlKeys(),
    UnicodeAsciiKeys(),
    JargonKeys(),
    IntercalKeys()
])


PLATFORM_KEYS = {
    'unix': unix_keys,
    'windows': windows_keys,
}
