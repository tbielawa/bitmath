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
        """KiB(1) looks correct in a terminal"""
        self.assertEqual(repr(self.kib), self.kib_repr)

    def test_whole_kib_str(self):
        """KiB(1) looks correct as a string"""
        self.assertEqual(str(self.kib), self.kib_str)

    def test_half_mib_repr(self):
        """MiB(0.5) looks correct in a terminal"""
        self.assertEqual(repr(self.half_mib), self.half_mib_repr)

    def test_half_mib_str(self):
        """MiB(0.5) looks correct as a string"""
        self.assertEqual(str(self.half_mib), self.half_mib_str)
