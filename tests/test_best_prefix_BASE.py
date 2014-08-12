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
Test for base (Bit/Byte) prefix guessing
"""

from . import TestCase
import bitmath


class TestBestPrefixBASE(TestCase):
    def test_byte_round_down(self):
        """BASE: 4 Bits (as a Byte()) round down into a Bit()"""
        # Half a byte is 4 bits
        half_byte = bitmath.Byte(bits=4)
        # Byte(0.5) should round down into Bit(4)
        self.assertIs(type(half_byte.best_prefix()), bitmath.Bit)

    def test_bit_round_up(self):
        """BASE: 2 Bytes (as a Bit()) round up into a Byte()"""
        # Two bytes is 16 bits
        two_bytes = bitmath.Bit(bytes=2)
        # Bit(16) should round up into Byte(2)
        self.assertIs(type(two_bytes.best_prefix()), bitmath.Byte)

    def test_byte_no_rounding(self):
        """BASE: 1 Byte (as a Byte()) best prefix is still a Byte()"""
        # One whole byte
        one_byte = bitmath.Byte(1)
        # Byte(1.0) should stay the same, Byte(1.0)
        self.assertIs(type(one_byte.best_prefix()), bitmath.Byte)
