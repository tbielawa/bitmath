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
Test parsing strings into bitmath objects
"""

from . import TestCase
import bitmath


class TestParse(TestCase):
    def test_parse_b(self):
        """parse_string works on bit strings"""
        self.assertEqual(
            bitmath.parse_string("123b"),
            bitmath.Bit(123))

    def test_parse_B(self):
        """parse_string works on byte strings"""
        self.assertEqual(
            bitmath.parse_string("321B"),
            bitmath.Byte(321))

    def test_parse_Gb(self):
        """parse_string works on gigabyte strings"""
        self.assertEqual(
            bitmath.parse_string("456Gb"),
            bitmath.Gb(456))

    def test_parse_MiB(self):
        """parse_string works on mebibyte strings"""
        self.assertEqual(
            bitmath.parse_string("654 MiB"),
            bitmath.MiB(654))

    def test_parse_bad_float(self):
        """parse_string can identify invalid float values"""
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23.45 kb")

    def test_parse_bad_unit(self):
        """parse_string can identify invalid prefix units"""
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23 GIB")

    def test_parse_bad_unit2(self):
        """parse_string can identify other prefix units"""
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23 QB")

    def test_parse_no_unit(self):
        """parse_string can identify strings without units at all"""
        with self.assertRaises(ValueError):
            bitmath.parse_string("12345")

    def test_parse_string_non_string_input(self):
        """parse_string can identify a non-string input"""
        with self.assertRaises(ValueError):
            bitmath.parse_string(12345)

    def test_parse_string_unicode(self):
        """parse_string can handle a unicode string"""
        self.assertEqual(
            bitmath.parse_string(u"750 GiB"),
            bitmath.GiB(750))
