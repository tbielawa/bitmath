# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright © 2014 Tim Bielawa <timbielawa@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Test for basic math operations
"""

import unittest
from . import TestCase

def _mul(input=None, mul=None):
    input * mul

class TestBasicMath(TestCase):
    from bitmath import *
    from numbers import Number

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

    def test_absolute_positive_value(self):
        """abs(PositiveObject) is positive"""
        self.assertEqual(self.KiB(1), abs(self.KiB(1)))

    def test_absolute_negative_value(self):
        """abs(NegativeObject) is positive"""
        self.assertEqual(self.KiB(1), abs(self.KiB(-1)))

    def test_inversion_to_negative(self):
        """Negating a positive makes a negative"""
        self.assertEqual(self.KiB(-1), -self.KiB(1))

    def test_inversion_to_positive(self):
        """Plus'ing a negative makes a positive"""
        self.assertEqual(self.KiB(1), +self.KiB(-1))

    ##################################################################
    # add
    def bitmath_add_bitmath_is_bitmath(self):
        """bitmath + bitmath = bitmath"""
        bm1 = self.KiB(1)
        bm2 = self.KiB(2)
        result = bm1 + bm2
        self.assertEqual(result, self.KiB(3))
        self.assertIsInstance(result, self.Byte)

    def test_bitmath_add_number_is_number(self):
        """bitmath + number = number"""
        bm1 = self.KiB(1)
        num1 = 2
        result = bm1 + num1
        self.assertEqual(result, 3.0)
        self.assertIsInstance(result, self.Number)

    def test_number_add_bitmath_is_number(self):
        """number + bitmath = number"""
        num1 = 2
        bm1 = self.KiB(1)
        result = num1 + bm1
        self.assertEqual(result, 3.0)
        self.assertIsInstance(result, self.Number)

    ##################################################################
    # sub
    def test_bitmath_sub_bitmath_is_bitmath(self):
        """bitmath - bitmath = bitmath"""
        bm1 = self.KiB(1)
        bm2 = self.KiB(2)
        result = bm1 - bm2
        self.assertEqual(result, self.KiB(-1))
        self.assertIsInstance(result, self.Byte)

    def test_bitmath_sub_number_is_number(self):
        """bitmath - number = number"""
        bm1 = self.KiB(1)
        num1 = 2
        result = bm1 - num1
        self.assertEqual(result, -1.0)
        self.assertIsInstance(result, self.Number)

    def test_number_sub_bitmath_is_number(self):
        """number - bitmath = number"""
        num1 = 2
        bm1 = self.KiB(1)
        result = num1 - bm1
        self.assertEqual(result, 1.0)
        self.assertIsInstance(result, self.Number)

    ##################################################################
    # mul
    def test_bitmath_mul_bitmath_is_bitmath(self):
        """bitmath * bitmath = unsupported"""
        bm1 = self.KiB(1)
        bm2 = self.KiB(2)
        test_values = {'input': bm1, 'mul': bm2}
        self.assertRaises(TypeError, _mul, **test_values)

    def test_bitmath_mul_number_is_bitmath(self):
        """bitmath * number = bitmath"""
        bm1 = self.KiB(1)
        num1 = 2
        result = bm1 * num1
        self.assertEqual(result, self.KiB(2))
        self.assertIsInstance(result, self.Byte)

    def test_number_mul_bitmath_is_number(self):
        """number * bitmath = number"""
        num1 = 2
        bm1 = self.KiB(1)
        result = num1 * bm1
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, self.Number)

    ##################################################################
    # div
    def test_bitmath_div_bitmath_is_number(self):
        """bitmath / bitmath = number"""
        bm1 = self.KiB(1)
        bm2 = self.KiB(2)
        result = bm1 / bm2
        self.assertEqual(result, 0.5)
        self.assertIsInstance(result, self.Number)

    def test_bitmath_div_number_is_bitmath(self):
        """bitmath / number = bitmath"""
        bm1 = self.KiB(1)
        num1 = 2
        result = bm1 / num1
        self.assertEqual(result, self.KiB(0.5))
        self.assertIsInstance(result, self.Byte)

    def test_number_div_bitmath_is_number(self):
        """number / bitmath = number"""
        num1 = 2
        bm1 = self.KiB(1)
        result = num1 / bm1
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, self.Number)
