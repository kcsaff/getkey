import unittest

from getkey.platforms import PlatformTest


class TestKeys(unittest.TestCase):
    def test_character_length_1(self):
        key = PlatformTest().key
        self.assertEqual(1, len(key.CTRL_A))

    def test_character_length_3(self):
        key = PlatformTest().key
        self.assertEqual(3, len(key.UP))
