# -*- coding: utf-8 -*-
# Initially taken from:
# http://code.activestate.com/recipes/134892/
# Thanks to Danny Yoo

from __future__ import absolute_import, print_function
import os
import sys
from .keynames import PLATFORM_KEYS


class Platform(object):
    def __init__(self, keys, interrupts=None):
        keys = keys or self.KEYS

        if isinstance(keys, str):
            keys = PLATFORM_KEYS[keys]
        self.key = self.keys = keys
        if interrupts is None:
            interrupts = self.INTERRUPTS
        self.interrupts = {
            self.keys.code(name): action
            for name, action in interrupts.items()
        }

        assert(
            self.__class__.getchar != Platform.getchar or
            self.__class__.getchars != Platform.getchars
        )

    def getkey(self, blocking=True):
        buffer = ''
        for c in self.getchars(blocking):
            buffer += c
            if buffer not in self.keys.escapes:
                break

        keycode = self.keys.canon(buffer)
        if keycode in self.interrupts:
            interrupt = self.interrupts[keycode]
            if isinstance(interrupt, BaseException) or \
                issubclass(interrupt, BaseException):
                raise interrupt
            else:
                raise NotImplementedError('Unimplemented interrupt: {!r}'
                                          .format(interrupt))
        return keycode

    # You MUST override at least one of the following
    def getchars(self, blocking=True):
        char = self.getchar(blocking)
        while char:
            yield char
            char = self.getchar(False)

    def getchar(self, blocking=True):
        for char in self.getchars(blocking):
            return char
        else:
            return None

    def bang(self):
        while True:
            code = self.getkey(True)
            name = self.keys.name(code) or '???'
            print('{} = {!r}'.format(name, code))


class PlatformUnix(Platform):
    KEYS = 'unix'
    INTERRUPTS = {'CTRL_C': KeyboardInterrupt}

    def __init__(self, keys=None, interrupts=None,
                 stdin=None, select=None, tty=None, termios=None):
        super(PlatformUnix, self).__init__(keys, interrupts)
        self.stdin = stdin or sys.stdin
        if not select:
            from select import select
        if not tty:
            import tty
        if not termios:
            import termios
        self.select = select
        self.tty = tty
        self.termios = termios

    def getchars(self, blocking=True):
        """Get characters on Unix."""

        old_settings = self.termios.tcgetattr(self.stdin)
        self.tty.setcbreak(self.stdin.fileno())
        try:
            if blocking:
                yield os.read(self.stdin.fileno(), 1)
            while self.select([self.stdin], [], [], 0)[0]:
                yield os.read(self.stdin.fileno(), 1)
        finally:
            self.termios.tcsetattr(
                self.stdin, self.termios.TCSADRAIN, old_settings
            )


class PlatformWindows(Platform):
    KEYS = 'windows'
    INTERRUPTS = {'CTRL_C': KeyboardInterrupt}

    def __init__(self, keys=None, interrupts=None, msvcrt=None):
        super(PlatformWindows, self).__init__(keys, interrupts)
        if msvcrt is None:
            import msvcrt
        self.msvcrt = msvcrt

    def getchars(self, blocking=True):
        """Get characters on Windows."""

        if blocking:
            yield self.msvcrt.getch()
        while self.msvcrt.kbhit():
            yield self.msvcrt.getch()


class PlatformTest(Platform):
    KEYS = 'unix'
    INTERRUPTS = {}

    def __init__(self, chars='', keys=None, interrupts=None):
        super(PlatformTest, self).__init__(keys, interrupts)
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
]


def platform(name=None, keys=None, interrupts=None):
    name = name or sys.platform
    for prefix, ctor in PLATFORMS:
        if name.startswith(prefix):
            return ctor(keys=keys, interrupts=interrupts)
    else:
        raise NotImplementedError('Unknown platform {!r}'.format(name))


