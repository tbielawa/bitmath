"""
Test for basic math operations
"""

from . import TestCase

class TestBasicMath(TestCase):
    from bitmath import *

    def setUp(self):
        self.kib_in_bytes = 1024
        self.kib_in_bits = 8192

    def test_type_raw_int_equality(self):
        """A bitmath type is equal to the value it's instanted with"""
        kib = self.KiB(1)
        self.assertEqual(kib, 1)

    def test_same_bitmath_types_equality(self):
        """Two same bitmath types are equal"""
        self.assertEqual(self.KiB(1), self.KiB(1))

    def test_different_bitmath_types_equality(self):
        """Two different bitmath types are equal"""
        self.assertEqual(self.KiB(1), self.Byte(self.kib_in_bytes))

    def test_add_same_type_equal_same_type(self):
        """Adding the same bitmath types is equal to result as the same type"""
        kib1 = self.KiB(1)
        kib2 = self.KiB(1)
        added_two_kib = kib1 + kib2
        two_kib = self.KiB(2)
        self.assertEqual(added_two_kib, two_kib)

    def test_add_different_types_equal_bitmath_type(self):
        """Adding two different bitmath types is equal to another type of the same size"""
        # One Kibibyte + 1024 Bytes = 2048 bytes = Byte(2048)
        kib1 = self.KiB(1)
        byte1 = self.Byte(1024)
        added_different_types = kib1 + byte1
        two_kib_in_bytes = self.Byte(2048)
        self.assertEqual(added_different_types, two_kib_in_bytes)

    def test_adding_with_different_base_units(self):
        """Adding a bit based type with a byte based type"""
        kib_sized_bit_from_bytes = self.Bit(self.kib_in_bits)
        kib = self.KiB(1)
        added = kib_sized_bit_from_bytes + kib
        two_kib = self.KiB(2)
        self.assertEqual(added, two_kib)

    def test_subtracting_with_different_base_units(self):
        """Subtracting a bit based type with a byte based type"""
        kib_sized_bit_from_bytes = self.Bit(self.kib_in_bits)
        kib = self.KiB(1)
        subtracted = kib_sized_bit_from_bytes - kib
        zero_kib = self.KiB(0)
        self.assertEqual(subtracted, zero_kib)

    def test_subtract_bitmath_types(self):
        """Subtracting two bitmath types"""
        kib1 = self.KiB(2)
        kib2 = self.Byte(512)
        # Result of subtracting kib1-kib2 => 2048-512 = 1536 bytes
        result_kib_in_bytes = self.Byte(1536)
        self.assertEqual(kib1 - kib2, result_kib_in_bytes)

    def test_multiply_bitmath_with_int(self):
        """Multiplying a bitmath types with an int"""
        # 3 KiB = 3072 bytes
        kib1 = self.KiB(3)
        kib_multiplied = kib1 * 3
        # 3 KiB * 3 = 9216 bytes
        self.assertEqual(kib_multiplied, self.Byte(9216))

    def test_multiply_bitmath_with_bitmath(self):
        """Multiplying a bitmath type with a bitmath type fails"""
        kib1 = self.KiB(3)
        kib2 = self.KiB(3)
        self.assertRaises(TypeError, lambda x, y: x* y, kib1, kib2)

    def test_divide_bitmath_type_with_int(self):
        """Dividing a bitmath type by an integer"""
        # 4KiB = 4096 Bytes
        kib4 = self.KiB(4)
        # 4KiB / 4 = 1024 Bytes
        result_kib = kib4 / 4
        self.assertEqual(result_kib, 1,
                         msg="result KiB %s(bytes) not equal to %s bytes" %
                         (result_kib, 1))
        self.assertEqual(result_kib, self.Byte(1024),
                         msg="result KiB %s(bytes) not equal to %s" %
                         (result_kib, self.Byte(1024)))

    def test_divide_bitmath_type_with_bitmath(self):
        """Dividing bitmath type with a bitmath type succeeds"""
        mib = self.MiB(1)
        quarter_mib = self.KiB(256)
        self.assertEqual(mib / quarter_mib, 4)
