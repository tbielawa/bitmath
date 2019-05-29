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
Test the click 'Bitmath' type integration
"""

from . import TestCase
import bitmath
from bitmath.integrations.bmclick import BitmathType, BITMATH
import click
from click.testing import CliRunner


class TestClickType(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_click_BitmathType_good_one_arg(self):
        @click.command()
        @click.argument('arg', type=BitmathType())
        def func(arg):
            click.echo(arg)

        result = self.runner.invoke(func, ['1000EB'])
        self.assertFalse(result.exception)
        self.assertEqual(result.output.splitlines(), [str(bitmath.EB(1000))])

    def test_click_BitmathType_good_one_opt(self):
        @click.command()
        @click.option('--opt', type=BitmathType())
        def func(opt):
            click.echo(opt)

        result = self.runner.invoke(func, ['--opt', '1007TB'])
        self.assertFalse(result.exception)
        self.assertEqual(result.output.splitlines(), [str(bitmath.TB(1007))])

    def test_click_BitmathType_good_two_args(self):
        @click.command()
        @click.argument('arg1', type=BitmathType())
        @click.argument('arg2', type=BitmathType())
        def func(arg1, arg2):
            click.echo(arg1)
            click.echo(arg2)

        result = self.runner.invoke(func, ['1337B', '0.001GiB'])
        self.assertFalse(result.exception)
        self.assertEqual(result.output.splitlines(), [str(bitmath.Byte(1337)),
                                                      str(bitmath.GiB(0.001))])

    def test_click_BitmathType_bad_wtfareyoudoing(self):
        @click.command()
        @click.argument('arg', type=BitmathType())
        def func(arg):
            click.echo(arg)

        result = self.runner.invoke(func, ['2098329324kdsjflksdjf'])
        self.assertTrue(result.exception)

    def test_click_BitmathType_good_spaces_in_value(self):
        @click.command()
        @click.argument('arg1', type=BitmathType())
        @click.argument('arg2', type=BitmathType())
        def func(arg1, arg2):
            click.echo(arg1)
            click.echo(arg2)

        result = self.runner.invoke(func, ['100 MiB', '200 KiB'])
        self.assertFalse(result.exception)
        self.assertEqual(result.output.splitlines(), [str(bitmath.MiB(100)),
                                                      str(bitmath.KiB(200))])

    def test_click_BitmathType_bad_spaces_in_value(self):
        @click.command()
        @click.argument('arg', type=BitmathType())
        def func(arg):
            click.echo(arg)

        result = self.runner.invoke(func, ['1000', 'EB'])
        self.assertTrue(result.exception)

    def test_click_BITMATH_good_one_arg(self):
        @click.command()
        @click.argument('arg', type=BITMATH)
        def func(arg):
            click.echo(arg)

        result = self.runner.invoke(func, ['1234.5 TiB'])
        self.assertFalse(result.exception)
        self.assertEqual(result.output.splitlines(), [str(bitmath.TiB(1234.5))])
