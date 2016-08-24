# -*- coding: utf-8 -*-
import unittest

from getkey.platforms import PlatformTest


def readchar_fn_factory(stream):

    v = [x for x in stream]

    def inner(blocking=False):
        return v.pop(0)
    return inner


class TestGetkey(unittest.TestCase):
    def test_basic_character(self):
        getkey = PlatformTest('a').getkey
        result = getkey()

        self.assertEqual('a', result)

    def test_string_instead_of_char(self):
        char = 'a'

        getkey = PlatformTest(char + 'bcde').getkey
        result = getkey()

        self.assertEqual(char, result)

    def test_special_combo_character(self):
        char = '\x1b\x01'

        getkey = PlatformTest(char + 'foo').getkey
        result = getkey()

        self.assertEqual(char, result)

    def test_special_key(self):
        char = '\x1b\x5b\x41'

        getkey = PlatformTest(char + 'foo').getkey
        result = getkey()

        self.assertEqual(char, result)

    def test_special_key_combo(self):
        char = '\x1b\x5b\x33\x5e'

        getkey = PlatformTest(char + 'foo').getkey
        result = getkey()

        self.assertEqual(char, result)

    def test_unicode_character(self):
        text = u'Ángel'

        getkey = PlatformTest(text).getkey
        result = getkey()

        self.assertEqual(u'Á', result)
