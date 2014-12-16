from . import TestCase
import bitmath

class TestParse(TestCase):
    def test_b(self):
        self.assertEqual(
            bitmath.parse_string("123b"),
            bitmath.Bit(123))

    def test_B(self):
        self.assertEqual(
            bitmath.parse_string("321B"),
            bitmath.Byte(321))

    def test_Gb(self):
        self.assertEqual(
            bitmath.parse_string("456Gb"),
            bitmath.Gb(456))

    def test_MiB(self):
        self.assertEqual(
            bitmath.parse_string("654 MiB"),
            bitmath.MiB(654))

    def test_bad_float(self):
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23.45 kb")

    def test_bad_unit(self):
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23 GIB")

    def test_bad_unit2(self):
        with self.assertRaises(ValueError):
            bitmath.parse_string("1.23 QB")
