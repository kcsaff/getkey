
# Which key(s) were pressed
# What chars to print (if any)
# Keycode(s) generating event


class Key(object):
    def __init__(self, name, unix=None, windows=None):


class Keyboard(object):
    pass


class KeyboardAnsi(Keyboard):
    ESCAPE = None
    F1 = None







class Key(object):
    __memo = dict()

    def __init__(self, name, chars, unix=None, windows=None):

        self.name = name
        self.unix = unix
        self.windows = windows
        if self.is_literal and not self.unix:
            self.unix = self.aliases
        if self.unix and not self.windows:
            self.windows = self.unix
        if self.is_literal and not self.windows:
            self.windows = self.aliases

        for alias in self.aliases:
            self.__memo[alias] = self

    @classmethod
    def get(cls, name, force_object=False):
        if name in cls.__memo:
            return cls.__memo[name]
        elif len(name) == 1:
            return cls([name]) if force_object else name
        else:
            raise KeyError('No key aliased {!r}'.format(name))

    @classmethod
    def all_defined(cls):
        return cls.__memo.values()

    @property
    def name(self):
        return self.aliases[0]

    def __repr__(self):
        if self.is_literal:
            return repr(self.name)
        else:
            return '<{}>'.format(self.name.upper())

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return other is self or str(other).lower() in self.aliases

    def __ne__(self, other):
        return not self.__eq__(other)


class Shift(object):
    def __call__(self, key):
        pass


class Keys(object):
    def __init__(self, force_object=False):
        self.force_object = force_object

    def __getattr__(self, attr):
        if len(attr) > 1:
            attr = attr.lower().replace('_', ' ')
        return Key.get(attr, force_object=self.force_object)


def control(char):




# cursors
UP = Key(['up'], ['\x1b\x5b\x41'])
DOWN = Key(['down'], ['\x1b\x5b\x42'])
RIGHT = Key(['right'], ['\x1b\x5b\x43'])
LEFT = Key(['left'], ['\x1b\x5b\x44'])
ENTER = Key(['enter', 'return', '\n', 'line feed', 'lf'], ['\n'])
CR = Key(['carriage return', '\r', 'cr'], ['\r'])
BACKSPACE = Key(['backspace'], ['\x7f'])
DELETE = Key(['delete'], ['\x1b[3~'])

KEY_CTRL_C = '\x03'

# common
SUPR = ''
SPACE = '\x20'
ESC = '\x1b'

# CTRL
CTRL_A = '\x01'
CTRL_B = '\x02'
CTRL_C = '\x03'
CTRL_D = '\x04'
CTRL_E = '\x05'
CTRL_F = '\x06'
CTRL_Z = '\x1a'

# ALT
ALT_A = '\x1b\x61'

# CTRL + ALT
CTRL_ALT_A = '\x1b\x01'

CTRL_ALT_SUPR = '\x1b\x5b\x33\x5e'

# other
F1 = '\x1b\x4f\x50'
F2 = '\x1b\x4f\x51'
F3 = '\x1b\x4f\x52'
F4 = '\x1b\x4f\x53'
F5 = '\x1b\x4f\x31\x35\x7e'
F6 = '\x1b\x4f\x31\x37\x7e'
F7 = '\x1b\x4f\x31\x38\x7e'
F8 = '\x1b\x4f\x31\x39\x7e'
F9 = '\x1b\x4f\x32\x30\x7e'
F10 = '\x1b\x4f\x32\x31\x7e'
F11 = '\x1b\x4f\x32\x33\x7e'
F12 = '\x1b\x4f\x32\x34\x7e'

INSERT = '\x1b\x5b\x32\x7e'
SUPR = '\x1b\x5b\x33\x7e'
