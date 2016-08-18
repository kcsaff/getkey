# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo
import os
import sys
from abc import ABCMeta, abstractmethod
from .keys import Key


class Platform(object):
    __metaclass__ = ABCMeta

    def __init__(self, codes):
        codes = codes or self.CODES
        if isinstance(codes, str):
            codes = _make_codes(codes)
        self.codes = codes
        self.escapes = _make_escapes(self.codes)

    def getkey(self, blocking=True):
        buffer = self.getchar(blocking)
        if not buffer:
            return ''

        while True:
            if buffer not in self.escapes:
                break
            c = self.getchar(False)
            if not c:
                break
            buffer += c

        if buffer in self.codes:
            return self.codes[buffer]
        else:
            return Key.get(buffer)

    @abstractmethod
    def getchar(self, blocking=True):
        raise NotImplementedError


def _make_codes(name):
    codes = dict()
    for key in Key.all_defined():
        keycodes = getattr(key, name) or ()
        for keycode in keycodes:
            codes[keycode] = key
    return codes


def _make_escapes(codes):
    escapes = set()
    for code in codes:
        for i in range(len(code)):
            escapes.add(code[:i])
    return escapes


class PlatformUnix(Platform):
    CODES = 'unix'

    def __init__(self, codes=None, stdin=sys.stdin, select=None, tty=None, termios=None):
        super(PlatformUnix, self).__init__(codes)
        self.stdin = stdin
        if not select:
            from select import select
        if not tty:
            import tty
        if not termios:
            import termios
        self.select = select
        self.tty = tty
        self.termios = termios

    def getchar(self, blocking=True):
        old_settings = self.termios.tcgetattr(self.stdin)
        self.tty.setcbreak(self.stdin.fileno())
        try:
            if blocking or self.select([self.stdin, ], [], [], 0.0)[0]:
                char = os.read(self.stdin.fileno(), 1)
                return char if type(char) is str else char.decode()
        finally:
            self.tcsetattr(sys.stdin, self.termios.TCSADRAIN, old_settings)


class PlatformWindows(Platform):
    CODES = 'windows'

    def __init__(self, codes=None, msvcrt=None):
        super(PlatformWindows, self).__init__(codes)
        if msvcrt is None:
            import msvcrt
        self.msvcrt = msvcrt

    def getchar(self, blocking=True):
        """Get a single character on Windows."""

        while self.msvcrt.kbhit():
            self.msvcrt.getch()
        ch = self.msvcrt.getch()
        while ch in '\x00\xe0':
            self.msvcrt.getch()
            ch = self.msvcrt.getch()
        return ch.decode()


class PlatformTest(Platform):
    CODES = 'unix'

    def __init__(self, chars, codes=None):
        super(PlatformTest, self).__init__(codes)
        self.chars = chars
        self.index = 0

    def getchar(self, blocking=True):
        if self.index >= len(self.chars) and not blocking:
            return ''
        else:
            char = self.chars[self.index]
            self.index += 1
            return char


PLATFORMS = [
    ('linux', PlatformUnix),
    ('darwin', PlatformUnix),
    ('win32', PlatformWindows),
    ('cygwin', PlatformWindows),
    ('test', PlatformTest),
]


def platform(name=None, codes=None):
    name = name or sys.platform
    for prefix, ctor in PLATFORMS:
        if name.startswith(prefix):
            return ctor(codes=codes)
    else:
        raise NotImplementedError('Unknown platform {!r}'.format(name))


