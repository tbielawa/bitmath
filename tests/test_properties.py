"""
Tests to verify that type properties are accessable and immutable
"""

from . import TestCase

def _add(input=None, add=None):
    print input, add
    input.value += add

class TestAttributeProperties(TestCase):
    from bitmath import *

    def setUp(self):
        self.kib = self.KiB(1)
        self.kib_bits = 8192
        self.kib_bytes = 1024
        self.kib_value = 1

    def test_read_bits(self):
        """Read the 'bits' property of a bitmath type"""
        self.assertEqual(self.kib.bits, self.kib_bits)

    def test_read_bytes(self):
        """Read the 'bytes' property of a bitmath type"""
        self.assertEqual(self.kib.bytes, self.kib_bytes)

    def test_read_value(self):
        """Read the 'value' property of a bitmath type"""
        self.assertEqual(self.kib.value, self.kib_value)

    def test_write_property_fails(self):
        """bitmath type's properties are read-only"""
        test_values = {'input': self.kib, 'add': 42}
        self.assertRaises(AttributeError, _add, **test_values)
