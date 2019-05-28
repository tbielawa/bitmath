# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright © 2014-2016 Tim Bielawa <timbielawa@gmail.com>
# See GitHub Contributors Graph for more information
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sub-license, and/or sell copies of the Software,
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

import bitmath
import click


class BitmathType(click.ParamType):
    """An parameter type for integrations with the click module.

For more information see https://click.palletsprojects.com/en/7.x/parameters/
and https://click.palletsprojects.com/en/7.x/options/#basic-value-options

Example usage of the click Bitmath type for a click argument:

  from bitmath.integrations.bmclick import BitmathType

  @click.command()
  @click.argument('size', type=BitmathType)
  def best_prefix(size):
      click.echo(size.best_prefix())

It can also be used for click options:

  from bitmath.integrations.bmclick import BitmathType

  @click.command()
  @click.option('--size', required=True, type=BitmathType)
  def best_prefix(size):
      click.echo(size.best_prefix())
"""
    name = 'bitmath'

    def convert(self, value, param, ctx):
        try:
            return bitmath.parse_string(value)
        except ValueError:
            self.fail("'%s' can not be parsed into a valid bitmath object" %
                      value)


BITMATH = BitmathType()
