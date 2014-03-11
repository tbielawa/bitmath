"""
Tests to verify that string representations are accurate
"""

from . import TestCase

class TestBasicMath(TestCase):
    from bitmath import *

    def setUp(self):
        self.kib = self.KiB(1)
        self.kib_repr = 'KiB(1.0)'
        self.kib_str = '1.0KiB'
        self.half_mib = self.MiB(0.5)
        self.half_mib_repr = 'MiB(0.5)'
        self.half_mib_str = '0.5MiB'

    def test_whole_kib_repr(self):
        self.assertEqual(repr(self.kib), self.kib_repr)

    def test_whole_kib_str(self):
        self.assertEqual(str(self.kib), self.kib_str)

    def test_half_mib_repr(self):
        self.assertEqual(repr(self.half_mib), self.half_mib_repr)

    def test_half_mib_str(self):
        self.assertEqual(str(self.half_mib), self.half_mib_str)
