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
Test for SI prefix guessing
"""

import unittest
from . import TestCase
import bitmath


class TestBestPrefixSI(TestCase):
    ##################################################################
    # These tests verify guessing for cases where the best
    # representation is only one order of magnitude different.

    def test_simple_round_up(self):
        """SI: 1 GB (as a MB()) rounds up into a GB()"""
        # Represent a Gigabyte as a large MB
        GB_in_MB = bitmath.MB(1024)
        # This should turn into a GB
        self.assertIs(type(GB_in_MB.best_prefix()), bitmath.GB)

    def test_simple_round_down(self):
        """SI: 1 MB (as a GB()) rounds down into a MB()"""
        # Represent one MB as a small GB
        MB_in_GB = bitmath.GB(bytes=1048576)
        # This should turn into a MB
        self.assertIs(type(MB_in_GB.best_prefix()), bitmath.MB)

    ##################################################################
    # These tests verify guessing for cases where the best
    # representation is more than one order of magnitude different.

    def test_multi_oom_round_up(self):
        """SI: A very large Kilobyte rounds up into a Petabyte"""
        large_kB = bitmath.kB.from_other(bitmath.PB(1))
        self.assertIs(type(large_kB.best_prefix()), bitmath.PB)

    def test_multi_oom_round_down(self):
        """SI: A very small Petabyte rounds down into a Kilobyte"""
        small_PB = bitmath.PB.from_other(bitmath.kB(1))
        self.assertIs(type(small_PB.best_prefix()), bitmath.kB)

    ##################################################################
    # These tests mirror the multi_oom ones, except for extreme cases
    # where even the largest unit available results in values with
    # more than 4 digits left of the radix point.

    def test_extreme_oom_round_up(self):
        """SI: 2048 EB (as a kB()) rounds up into an EB()"""
        huge_kB = bitmath.kB.from_other(bitmath.EB(1))
        self.assertIs(type(huge_kB.best_prefix()), bitmath.EB)

    def test_extreme_oom_round_down(self):
        """SI: 1 Bit (as a EB()) rounds down into a Bit()"""
        tiny_EB = bitmath.EB.from_other(bitmath.Bit(1))
        self.assertIs(type(tiny_EB.best_prefix()), bitmath.Bit)
