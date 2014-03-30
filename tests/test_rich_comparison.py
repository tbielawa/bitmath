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
Test for rich comparison operations: LT, LE, EQ, NE, GT, GE
"""

import unittest
from . import TestCase
from bitmath import *

class TestRichComparison(TestCase):
    def setUp(self):
        self.kib = KiB(1)
        self.mib = MiB(1)
        self.gib = GiB(1)

    # def test_type_raw_int_equality(self):
    #     """A bitmath type is equal to the value it's instanted with"""
    #     kib = self.KiB(1)
    #     self.assertEqual(kib, 1)

    def test_less_than(self):
        """One KiB is less than one MiB"""
        self.assertLess(self.kib, self.mib)

    def test_less_than_equal(self):
        """Smaller or equal is less than or equal to one MiB"""
        # True - 1 KiB is less than 1 MiB
        self.assertLessEqual(self.kib, self.mib)
        # True - 1024 KiB is equal to 1 MiB
        self.assertLessEqual(KiB(1024), self.mib)

    def test_greater_than(self):
        """1 GiB is greater than 1 Mib"""
        self.assertGreater(self.gib, self.mib)

    def test_greater_than_equal(self):
        """Greater or equal is more than or equal to one MiB"""
        # True - 1 GiB is greater than 1 MiB
        self.assertGreaterEqual(self.gib, self.mib)
        # True - 1024 KiB is equal to 1 MiB
        self.assertGreaterEqual(self.mib, GiB(1 / 1024.0))

    def test_equal(self):
        """Two equal values are actually equal"""
        self.assertEqual(self.mib, KiB(1024))

    def test_not_equal(self):
        """Unequal objects aren't equal"""
        self.assertNotEqual(self.kib, self.gib)
