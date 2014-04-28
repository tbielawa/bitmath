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
Reference material:

Prefixes for binary multiples:
http://physics.nist.gov/cuu/Units/binary.html

decimal and binary prefixes:
man 7 units (from the Linux Documentation Project 'man-pages' package)
"""


import numbers

__all__ = ['Bit', 'Byte', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'Kib', 'Mib', 'Gib', 'Tib', 'Pib', 'Eib', 'kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb']


SI_PREFIXES = ['k', 'M', 'G', 'T', 'P', 'E']
SI_STEPS = {
    'Bit': 1 / 8.0,
    'Byte': 1,
    'k': 1000,
    'M': 1000000,
    'G': 1000000000,
    'T': 1000000000000,
    'P': 1000000000000000,
    'E': 1000000000000000000
}

NIST_PREFIXES = ['Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei']
NIST_STEPS = {
    'Bit': 1 / 8.0,
    'Byte': 1,
    'Ki': 1024,
    'Mi': 1048576,
    'Gi': 1073741824,
    'Ti': 1099511627776,
    'Pi': 1125899906842624,
    'Ei': 1152921504606846976
}


######################################################################
# First, the bytes...


class Byte(object):
    """The base class for all the other prefix classes

Byte based types fundamentally operate on self._bit_value"""

    def __init__(self, value=0, bytes=None, bits=None):
        """Instantiate with `value` by the unit, in plain bytes, or
bits. Don't supply more than one keyword."""
        self._do_setup()
        if bytes:
            # We were provided with the fundamental base unit, no need
            # to normalize
            self._byte_value = bytes
            self._bit_value = bytes * 8.0
        elif bits:
            # We were *ALMOST* given the fundamental base
            # unit. Translate it into the fundamental unit then
            # normalize.
            self._byte_value = bits / 8.0
            self._bit_value = bits
        else:
            # We were given a value representative of this *prefix
            # unit*. We need to normalize it into the number of bytes
            # it represents.
            self._norm(value)

        # We have the fundamental unit figured out. Set the 'pretty' unit
        self._set_prefix_value()

    def _set_prefix_value(self):
        self.prefix_value = self._to_prefix_value(self._byte_value)

    def _to_prefix_value(self, value):
        """Return the number of bits/bytes as they would look like if we
converted *to* this unit"""
        return value / float(self._unit_value)

    def _setup(self):
        return (2, 0, 'Byte')

    def _do_setup(self):
        """Setup basic parameters for this class"""
        """`base` is the numeric base which when raised to `power` is
equivalent to 1 unit of the corresponding prefix. I.e., base=2,
power=10 represents 2^10, which is the NIST Binary Prefix for 1 Kibibyte.

Likewise, for the SI prefix classes `base` will be 10, and the `power`
for the Kilobyte is 3."""
        (self._base, self._power, self._name) = self._setup()
        self._unit_value = self._base ** self._power

    def _norm(self, value):
        """Normalize the input value into the fundamental unit for this prefix
type"""
        self._byte_value = value * self._unit_value
        self._bit_value = self._byte_value * 8.0

    @property
    def bits(self):
        """Return the number of bits in an instance"""
        return self._bit_value

    @property
    def bytes(self):
        """Return the number of bytes in an instance"""
        return self._byte_value

    @property
    def value(self):
        """Returns the "prefix" value of an instance"""
        return self.prefix_value

    @property
    def binary(self):
        """Returns the binary representation of an instance in binary 1s and
0s. Note that for very large numbers this will mean a lot of 1s and
0s. For example, GiB(100) would be represented as:

0b1100100000000000000000000000000000000000

That leading '0b' is normal. That's how Python represents binary."""
        return bin(int(self.bits))

    @property
    def bin(self):
        """Alias for instance.binary. Returns the binary representation of an
instance in binary 1s and 0s."""
        return self.binary

    @classmethod
    def from_other(cls, item):
        """Factory function to return instances of `item` converted in a new
instance of `cls`. Because this is a class method, it may be called
from any bitmath class object without the need to explicitly
instantiate the class ahead of time.

*Implicit Parameter:*
- `cls` A bitmath class, implicitly set to the class of the class
  object it is called on

*User Supplied Parameter:*
- `item` A bitmath class instance

*Example:*
>>> import bitmath
>>> kib = bitmath.KiB.from_other(MiB(1))
>>> print kib
KiB(1024.0)
"""
        return cls(bits=item.bits)

    ######################################################################
    # The following implement the Python datamodel customization methods
    #
    # Reference: http://docs.python.org/2.7/reference/datamodel.html#basic-customization

    def __repr__(self):
        """Representation of this object as you would expect to see in an
intrepreter"""
        return "%s(%s)" % \
            (self._name, self.prefix_value)

    def __str__(self):
        """String representation of this object"""
        return "%s%s" % \
            (self.prefix_value, self._name)

    ##################################################################

    def to_Bit(self):
        return Bit(self._bit_value)

    def to_Byte(self):
        return Byte(self._byte_value / float(NIST_STEPS['Byte']))

    ##################################################################

    def to_KiB(self):
        return KiB(bits=self._bit_value)

    def to_Kib(self):
        return Kib(bits=self._bit_value)

    def to_kB(self):
        return kB(bits=self._bit_value)

    def to_kb(self):
        return kb(bits=self._bit_value)

    ##################################################################

    def to_MiB(self):
        return MiB(bits=self._bit_value)

    def to_Mib(self):
        return Mib(bits=self._bit_value)

    def to_MB(self):
        return MB(bits=self._bit_value)

    def to_Mb(self):
        return Mb(bits=self._bit_value)

    ##################################################################

    def to_GiB(self):
        return GiB(bits=self._bit_value)

    def to_Gib(self):
        return Gib(bits=self._bit_value)

    def to_GB(self):
        return GB(bits=self._bit_value)

    def to_Gb(self):
        return Gb(bits=self._bit_value)

    ##################################################################

    def to_TiB(self):
        return TiB(bits=self._bit_value)

    def to_Tib(self):
        return Tib(bits=self._bit_value)

    def to_TB(self):
        return TB(bits=self._bit_value)

    def to_Tb(self):
        return Tb(bits=self._bit_value)

    ##################################################################

    def to_PiB(self):
        return PiB(bits=self._bit_value)

    def to_Pib(self):
        return Pib(bits=self._bit_value)

    def to_PB(self):
        return PB(bits=self._bit_value)

    def to_Pb(self):
        return Pb(bits=self._bit_value)

    ##################################################################

    def to_EiB(self):
        return EiB(bits=self._bit_value)

    def to_Eib(self):
        return Eib(bits=self._bit_value)

    def to_EB(self):
        return EB(bits=self._bit_value)

    def to_Eb(self):
        return Eb(bits=self._bit_value)

    ##################################################################

    def __lt__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value < other
        else:
            return self._byte_value < other.bytes

    def __le__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value <= other
        else:
            return self._byte_value <= other.bytes

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value == other
        else:
            return self._byte_value == other.bytes

    def __ne__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value != other
        else:
            return self._byte_value != other.bytes

    def __gt__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value > other
        else:
            return self._byte_value > other.bytes

    def __ge__(self, other):
        if isinstance(other, numbers.Number):
            return self.prefix_value >= other
        else:
            return self._byte_value >= other.bytes

    ##################################################################
    # Basic math operations
    ##################################################################

    # Reference: http://docs.python.org/2.7/reference/datamodel.html#emulating-numeric-types

    """These methods are called to implement the binary arithmetic
operations (+, -, *, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For
instance, to evaluate the expression x + y, where x is an instance of
a class that has an __add__() method, x.__add__(y) is called. The
__divmod__() method should be the equivalent to using __floordiv__()
and __mod__(); it should not be related to __truediv__() (described
below). Note that __pow__() should be defined to accept an optional
third argument if the ternary version of the built-in pow() function
is to be supported.object.__complex__(self)
"""

    def __add__(self, other):
        """Supported operations with result types:

- bm + bm = bm
- bm + num = num
- num + bm = num (see radd)
"""
        if isinstance(other, numbers.Number):
            # bm + num
            return other + self.value
        else:
            # bm + bm
            total_bytes = self._byte_value + other.bytes
            return (type(self))(bytes=total_bytes)

    def __sub__(self, other):
        """Supported operations with result types:

- bm - bm = bm
- bm - num = num
- num - bm = num (see rsub)
"""
        if isinstance(other, numbers.Number):
            # bm - num
            return self.value - other
        else:
            # bm - bm
            total_bytes = self._byte_value - other.bytes
            return (type(self))(bytes=total_bytes)

    def __mul__(self, other):
        """Supported operations with result types:

- bm1 * bm2 = bm1
- bm * num = bm
- num * bm = num (see rmul)
"""
        if isinstance(other, numbers.Number):
            # bm * num
            result = self._byte_value * other
            return (type(self))(bytes=result)
        else:
            # bm1 * bm2
            #
            # Need to figure out exactly how to calculate this.
            return NotImplemented

    """The division operator (/) is implemented by these methods. The
__truediv__() method is used when __future__.division is in effect,
otherwise __div__() is used. If only one of these two methods is
defined, the object will not support division in the alternate
context; TypeError will be raised instead."""

    def __div__(self, other):
        """Supported operations with result types:

- bm1 / bm2 = num
- bm / num = bm
- num / bm = num (see rdiv)
"""
        if isinstance(other, numbers.Number):
            # bm / num
            result = self._byte_value / other
            return (type(self))(bytes=result)
        else:
            # bm1 / bm2
            return self._byte_value / float(other.bytes)

    def __truediv__(self, other):
        # TODO: Fix truediv for num / bm
        # https://github.com/tbielawa/bitmath/issues/2
        return self.__div__(other)

    # def __floordiv__(self, other):
    #     return NotImplemented

    # def __mod__(self, other):
    #     return NotImplemented

    # def __divmod__(self, other):
    #     return NotImplemented

    # def __pow__(self, other, modulo=None):
    #     return NotImplemented

    ##################################################################

    """These methods are called to implement the binary arithmetic
operations (+, -, *, /, %, divmod(), pow(), **, <<, >>, &, ^, |) with
reflected (swapped) operands. These functions are only called if the
left operand does not support the corresponding operation and the
operands are of different types. [2] For instance, to evaluate the
expression x - y, where y is an instance of a class that has an
__rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns
NotImplemented.

These are the add/sub/mul/div methods for syntax where a number type
is given for the LTYPE and a bitmath object is given for the
RTYPE. E.g., 3 * MiB(3), or 10 / GB(42)
"""

    def __radd__(self, other):
        # num + bm = num
        return other + self.value

    def __rsub__(self, other):
        # num - bm = num
        return other - self.value

    def __rmul__(self, other):
        # num * bm = num
        return other * self.value

    def __rdiv__(self, other):
        # num / bm = num
        return other / float(self.value)

    """Called to implement the built-in functions complex(), int(),
long(), and float(). Should return a value of the appropriate type.

If one of those methods does not support the operation with the
supplied arguments, it should return NotImplemented.

For bitmath purposes, these methods return the int/long/float
equivalent of the this instances prefix unix value. That is to say:

    - int(KiB(3.336)) would return 3
    - long(KiB(3.336)) would return 3L
    - float(KiB(3.336)) would return 3.336
"""

    def __int__(self):
        """Return this instances prefix unit as an integer"""
        return int(self.prefix_value)

    def __long__(self):
        """Return this instances prefix unit as a long integer"""
        return long(self.prefix_value)

    def __float__(self):
        """Return this instances prefix unit as a floating point number"""
        return float(self.prefix_value)

    ##################################################################
    # Bitwise operations
    ##################################################################

    def __lshift__(self, other):
        """Left shift, ex: 100 << 2

A left shift by n bits is equivalent to multiplication by pow(2,
n). A long integer is returned if the result exceeds the range of
plain integers."""
        shifted = int(self.bits) << other
        return type(self)(bits=shifted)

    def __rshift__(self, other):
        """Right shift, ex: 100 >> 2

A right shift by n bits is equivalent to division by pow(2, n)."""
        shifted = int(self.bits) >> other
        return type(self)(bits=shifted)

    def __and__(self, other):
        """"Bitwise and, ex: 100 & 2

bitwise and". Each bit of the output is 1 if the corresponding bit
of x AND of y is 1, otherwise it's 0."""
        andd = int(self.bits) & other
        return type(self)(bits=andd)

    def __xor__(self, other):
        """Bitwise xor, ex: 100 ^ 2

Does a "bitwise exclusive or". Each bit of the output is the same
as the corresponding bit in x if that bit in y is 0, and it's the
complement of the bit in x if that bit in y is 1."""
        xord = int(self.bits) ^ other
        return type(self)(bits=xord)

    def __or__(self, other):
        """Bitwise or, ex: 100 | 2

Does a "bitwise or". Each bit of the output is 0 if the corresponding
bit of x AND of y is 0, otherwise it's 1."""
        ord = int(self.bits) | other
        return type(self)(bits=ord)

    ##################################################################

    def __neg__(self):
        """The negative version of this instance"""
        return (type(self))(-abs(self.prefix_value))

    def __pos__(self):
        return (type(self))(abs(self.prefix_value))

    def __abs__(self):
        return (type(self))(abs(self.prefix_value))

    # def __invert__(self):
    #     """Called to implement the unary arithmetic operations (-, +, abs()
    #     and ~)."""
    #     return NotImplemented


######################################################################
# NIST Prefixes for Byte based types
class KiB(Byte):
    def _setup(self):
        return (2, 10, 'KiB')


class MiB(Byte):
    def _setup(self):
        return (2, 20, 'MiB')


class GiB(Byte):
    def _setup(self):
        return (2, 30, 'GiB')


class TiB(Byte):
    def _setup(self):
        return (2, 40, 'TiB')


class PiB(Byte):
    def _setup(self):
        return (2, 50, 'PiB')


class EiB(Byte):
    def _setup(self):
        return (2, 60, 'EiB')


######################################################################
# SI Prefixes for Byte based types
class kB(Byte):
    def _setup(self):
        return (10, 3, 'kB')


class MB(Byte):
    def _setup(self):
        return (10, 6, 'MB')


class GB(Byte):
    def _setup(self):
        return (10, 9, 'GB')


class TB(Byte):
    def _setup(self):
        return (10, 12, 'TB')


class PB(Byte):
    def _setup(self):
        return (10, 15, 'PB')


class EB(Byte):
    def _setup(self):
        return (10, 18, 'EB')


######################################################################
# And now the bit types
class Bit(Byte):
    """Bit based types fundamentally operate on self._bit_value"""

    def _set_prefix_value(self):
        self.prefix_value = self._to_prefix_value(self._bit_value)

    def _setup(self):
        return (2, 0, 'Bit')

    def _norm(self, value):
        """Normalize the input value into the fundamental unit for this prefix
type"""
        self._bit_value = value * self._unit_value
        self._byte_value = self._bit_value / 8.0


######################################################################
# NIST Prefixes for Bit based types
class Kib(Bit):
    def _setup(self):
        return (2, 10, 'Kib')


class Mib(Bit):
    def _setup(self):
        return (2, 20, 'Mib')


class Gib(Bit):
    def _setup(self):
        return (2, 30, 'Gib')


class Tib(Bit):
    def _setup(self):
        return (2, 40, 'Tib')


class Pib(Bit):
    def _setup(self):
        return (2, 50, 'Pib')


class Eib(Bit):
    def _setup(self):
        return (2, 60, 'Eib')


######################################################################
# SI Prefixes for Bit based types
class kb(Bit):
    def _setup(self):
        return (10, 3, 'kb')


class Mb(Bit):
    def _setup(self):
        return (10, 6, 'Mb')


class Gb(Bit):
    def _setup(self):
        return (10, 9, 'Gb')


class Tb(Bit):
    def _setup(self):
        return (10, 12, 'Tb')


class Pb(Bit):
    def _setup(self):
        return (10, 15, 'Pb')


class Eb(Bit):
    def _setup(self):
        return (10, 18, 'Eb')
