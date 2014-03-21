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
Test to verify the bitmath.Type.to_Type() conversions work
"""

from . import TestCase

class TestBasicMath(TestCase):
    from bitmath import NIST_STEPS, NIST_PREFIXES
    from bitmath import *

    def setUp(self):
        self.bit = self.Bit(1)
        self.byte = self.Byte(1)
        # NIST units
        self.kib = self.KiB(1)
        self.mib = self.MiB(1)
        self.gib = self.GiB(1)
        self.tib = self.TiB(1)
        self.pib = self.PiB(1)
        self.eib = self.EiB(1)

        # SI units
        self.kb = self.kB(1)
        self.mb = self.MB(1)
        self.gb = self.GB(1)
        self.tb = self.TB(1)
        self.pb = self.PB(1)
        self.eb = self.EB(1)

    def test_to_same_unit(self):
        """bitmath type converted to the same unit is properly converted"""
        to_kib = self.kib.to_KiB()
        self.assertIsInstance(to_kib, self.KiB)

    def test_to_KiB(self):
        """Convert a bitmath MiB into a KiB"""
        to_kib = self.mib.to_KiB()
        self.assertIsInstance(to_kib, self.KiB)

    def test_to_MiB(self):
        """Convert a bitmath GiB into a MiB"""
        to_mib = self.gib.to_MiB()
        self.assertIsInstance(to_mib, self.MiB)

    def test_to_GiB(self):
        """Convert a bitmath TiB into a GiB"""
        to_gib = self.tib.to_GiB()
        self.assertIsInstance(to_gib, self.GiB)

    def test_to_TiB(self):
        """Convert a bitmath PiB into a TiB"""
        to_tib = self.pib.to_TiB()
        self.assertIsInstance(to_tib, self.TiB)

    def test_to_PiB(self):
        """Convert a bitmath TiB into a PiB"""
        to_pib = self.tib.to_PiB()
        self.assertIsInstance(to_pib, self.PiB)

    def test_to_EiB(self):
        """Convert a bitmath PiB into a EiB"""
        to_eib = self.pib.to_EiB()
        self.assertIsInstance(to_eib, self.EiB)

    def test_to_mib_from_bit(self):
        """Convert a bitmath Bit into a MiB"""
        to_mib = self.bit.to_MiB()
        self.assertIsInstance(to_mib, self.MiB)

    def test_converted_up_bitmath_value_equivalency(self):
        """Converted up type has an equivalent value to the original"""
        # Take a KiB, make a MiB from it. Test their equality
        to_mib = self.kib.to_MiB()
        self.assertEqual(self.kib, to_mib)

        # Two tests, to be "thorough"
        to_gib = self.mib.to_GiB()
        self.assertEqual(self.mib, to_gib)

    def test_converted_down_bitmath_value_equivalency(self):
        """Converted down type has an equivalent value to the original"""
        # Take a MiB, make a KiB from it. Test their equality
        to_kib = self.mib.to_KiB()
        self.assertEqual(to_kib, self.mib)

    def test_convert_nist_to_si(self):
        """Convert an NIST unit into an SI unit"""
        kb_from_kib = self.kib.to_kB()
        self.assertIs(type(kb_from_kib), self.kB)

    def test_convert_si_to_nist(self):
        """Convert an SI unit into an NIST unit"""
        kib_from_kb = self.kb.to_KiB()
        self.assertIs(type(kib_from_kb), self.KiB)
