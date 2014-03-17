"""
Test to verify the int/float/long conversions work correctly
"""

from . import TestCase

class TestBasicMath(TestCase):
    from bitmath import *

    def test_to_int(self):
        """int(bitmath) returns an int"""
        gib = self.GiB(1337.8)
        self.assertIsInstance(int(gib), int)

    def test_to_float(self):
        """float(bitmath) returns a float"""
        gib = self.GiB(1337.8)
        self.assertIsInstance(float(gib), float)

    def test_to_long(self):
        """long(bitmath) returns a long"""
        gib = self.GiB(1337.8)
        self.assertIsInstance(long(gib), long)
