# -*- coding: iso-8859-15 -*-
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

"""Reference material:

Prefixes for binary multiples:
http://physics.nist.gov/cuu/Units/binary.html

decimal and binary prefixes:
man 7 units (from the Linux Documentation Project 'man-pages' package)


Random side note: These are prefixes because they modify the 'byte' or
'bit' unit. They don't appear before the numerical value they
describe.


This is just me venting: people need to get their acts
together. Really, what do these different things even mean? 5K, 5KB,
5Kbit, 5Kb, 5kB. Is it even possible to figure out what mean intend to
say? Lets lay down the ground rules for this module.

Parsing rules:

* All whitespace is removed before parsing begins.

* Input should follow the pattern: INTEGER :: [PREFIX] :: [UNIT]
- PREFIX and UNIT are optional. They are not mutually exclusive.

* Explicitly spelling out 'bit' or 'byte' will have the desired
  affect. This rule is case insensitive.

* Values beginning with an item in NIST_PREFIXES are interpreted as
  binary prefixes.

* Prefixes followed by 'b' will assume 'bit'.

* Prefixes followed by 'B' will assume 'byte' (8 bits).

* If the previous rule doesn't match, then: after the integer
  component, a grouping of all alphabetical characters is formed which
  extends to the end of the string, or the first occurance of a 'b' or
  'B' character. This grouping is searched for in SI_PREFIXES.

- /\d+[ac-z]b?/i

- For the purpose of this module, we will be ignoring the fact that
  the SI standard which defines the 'kilo' prefix as the lower-case
  'k' character. I.e., 1Kb and 1kb will be equivalent (both represent
  10^3 bits)

* Prefixes given without any following base unit (e.g., 1024K) assume
  the input is intended to be interpreted as an NIST unit prefix.

- Furthermore, to reward you for being lazy, the module assumes the
  input is in bytes. For example, given 1024K, the module interprets
  this as 1024KiB.



Therefore, 1kb and 1Kb will be equivalent. Whereas, 1kb and 1kB are
different. The former represents 10^3 bits, the latter represents 10^3
bytes. (10^3 * 8)

Finally,

"""


SI_PREFIXES = ['k', 'K', 'M']
NIST_PREFIXES = ['Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei']


def parse_size(size):
    numeric_value


class Bit(object):
    """The base class for all the other prefix classes"""
    def __init__(self, value='0b'):
        """If `value` is given without a prefix, we default to assuming bits."""
        self.intvalue = 0
        self.prefix = 'b'
        self._norm(

    def _norm(self):
        """Normalize the input value into a common base value"""
        raise NotImplementedError

    def _parse(self):

    def _guess_prefix(self, prefix):
        """Figure out which system the number is given in: NIST Binary, or
SI. Well... take our best shot at it anyway."""
        raise NotImplementedError

    # Reference: http://docs.python.org/2.7/reference/datamodel.html#basic-customization

    def __repr__(self):
        """Called by the repr() built-in function and by string conversions
(reverse quotes) to compute the "official" string representation of an
object. If at all possible, this should look like a valid Python
expression that could be used to recreate an object with the same
value (given an appropriate environment). If this is not possible, a
string of the form <...some useful description...> should be
returned. The return value must be a string object. If a class defines
__repr__() but not __str__(), then __repr__() is also used when an
"informal" string representation of instances of that class is
required."""
        return "Bit(%s)" % self.value

    def __str__(self):
        """Called by the str() built-in function and by the print statement to
compute the "informal" string representation of an object. This
differs from __repr__() in that it does not have to be a valid Python
expression: a more convenient or concise representation may be used
instead. The return value must be a string object."""
        return "Bit(%s)" % self.value

    # Reference: http://docs.python.org/2.7/reference/datamodel.html#emulating-numeric-types

    """These methods are called to implement the binary arithmetic
operations (+, -, *, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For
instance, to evaluate the expression x + y, where x is an instance of
a class that has an __add__() method, x.__add__(y) is called. The
__divmod__() method should be the equivalent to using __floordiv__()
and __mod__(); it should not be related to __truediv__() (described
below). Note that __pow__() should be defined to accept an optional
third argument if the ternary version of the built-in pow() function
is to be supported.

If one of those methods does not support the operation with the
supplied arguments, it should return NotImplemented."""

    def __add__(self, other):
        return NotImplemented

    def __sub__(self, other):
        return NotImplemented

    def __mul__(self, other):
        return NotImplemented

    def __floordiv__(self, other):
        return NotImplemented

    def __mod__(self, other):
        return NotImplemented

    def __divmod__(self, other):
        return NotImplemented

    def __pow__(self, other, modulo=None):
        return NotImplemented

    def __lshift__(self, other):
        return NotImplemented

    def __rshift__(self, other):
        return NotImplemented

    def __and__(self, other):
        return NotImplemented

    def __xor__(self, other):
        return NotImplemented

    def __or__(self, other):
        return NotImplemented

    """The division operator (/) is implemented by these methods. The
__truediv__() method is used when __future__.division is in effect,
otherwise __div__() is used. If only one of these two methods is
defined, the object will not support division in the alternate
context; TypeError will be raised instead."""

    def __div__(self, other):
        return NotImplemented

    def __truediv__(self, other):
        return NotImplemented

    def __neg__(self):
        return NotImplemented

    def __pos__(self):
        return NotImplemented

    def __abs__(self):
        return NotImplemented

    def __invert__(self):
        """Called to implement the unary arithmetic operations (-, +, abs()
and ~)."""
        return NotImplemented
