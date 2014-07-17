Instances
#########

.. _instance_attributes:

Instance Attributes
*******************

bitmath objects have several instance attributes:

- ``base`` - The mathematical base of the unit of the instance (this will be **2** or **10**)
- ``binary`` - The `Python binary representation <https://docs.python.org/2/library/functions.html#bin>`_ of the instance's value (in bits). ``bin`` is an alias for ``binary``
- ``bits`` - The number of bits in the object
- ``bytes`` - The number of bytes in the object
- ``power`` - The mathematical power the ``base`` of the unit of the instance is raised to
- ``system`` The system of units used to measure this instance (``NIST`` or ``SI``)
- ``value`` - The value of the instance in **PREFIX** units
- ``unit`` - The string representation of this prefix unit (such as ``MiB`` or ``kb``)

The following is an example of how to access these attributes and what
you can expect their printed representation to look like:

.. code-block:: python
   :linenos:

   In [13]: dvd_capacity = GB(4.7)

   In [14]: print "Capacity in bits: %s\nbytes: %s\n" % \
                (dvd_capacity.bits, dvd_capacity.bytes)

      Capacity in bits: 37600000000.0
      bytes: 4700000000.0

   In [15]: dvd_capacity.value

   Out[16]: 4.7

   In [17]: dvd_capacity.bin

   Out[17]: '0b100011000001001000100111100000000000'

   In [18]: dvd_capacity.binary

   Out[18]: '0b100011000001001000100111100000000000'



Instance Methods
****************

bitmath objects come with two basic methods: ``to_THING()`` and
``format()``.


to_THING()
==========

Like the available classes, there are 24 ``to_THING()`` methods
available. ``THING`` is any of the bitmath classes. You can even
``to_THING()`` an instance into itself again:


.. code-block:: python
   :linenos:

   In [1]: from bitmath import *

   In [2]: one_mib = MiB(1)

   In [3]: one_mib_in_kb = one_mib.to_kb()

   In [4]: one_mib == one_mib_in_kb

   Out[4]: True

   In [5]: another_mib = one_mib.to_MiB()

   In [6]: print one_mib, one_mib_in_kb, another_mib

   1.0MiB 8388.608kb 1.0MiB

   In [7]: six_TB = TB(6)

   In [8]: six_TB_in_bits = six_TB.to_Bit()

   In [9]: print six_TB, six_TB_in_bits

   6.0TB 4.8e+13Bit

   In [10]: six_TB == six_TB_in_bits

   Out[10]: True


format()
========

bitmath instances come with a verbose built-in string representation:

.. code-block:: python

   In [1]: from bitmath import *

   In [2]: leet_bits = Bit(1337)

   In [3]: print leet_bits
   1337.0Bit

However, for instances which aren't whole numbers (as in ``MiB(1/3.0)
== 0.333333333333MiB``, etc), their representation can be undesirable.

The ``format`` method gives you complete control over the instance's
representation. All of the :ref:`instances attributes
<instance_attributes>` are available to use when choosing a
representation.


The following are some common use cases of the ``format`` method.


Setting Decimal Precision
-------------------------

By default, bitmath instances will print to a fairly long precision
for values which are not whole multiples of their prefix unit. In most
use cases, simply printing out the first 2 or 3 digits of precision is
acceptable.

The following examples will show us how to print out a bitmath
instance in a more human readable way, by limiting the decimal
precision to 2 digits.

First, for reference, the default formatting:

.. code-block:: python
   :linenos:

   In [1]: from bitmath import *

   In [2]: ugly_number = MB(50).to_MiB() / 8.0

   In [3]: print ugly_number
   5.96046447754MiB

Now, let's use the ``format`` method to limit that to two digits of
precision:

.. code-block:: python

   In [7]: print ugly_number.format("{value:.2f}{unit}")
   5.96MiB

You may be asking yourself where these ``{value:.2f}`` and ``{unit}``
strings came from. These are part of the `Format Specification
Mini-Language
<https://docs.python.org/2/library/string.html#format-specification-mini-language>`_
which is part of the Python standard library. To be explicitly clear
about what's going on here, let's break the first specifier
(``{value:.2f}``) down into it's component parts::

   {value:.2f}
      ↑  ↑↑↑↑
      |  |||\---- The "f" says to format this as a floating point type
      |  ||\----- The 2 indicates we want 2 digits of precision (default is 6)
      |  |\------ The '.' character must precede the precision specifier for floats
      |  \------- The : separates the attribute name from the formatting specification
      \---------- The name of the attribute to print

The second specifier (``{unit}``) says to format the ``unit``
attribute as a string (string is the defalt type when no type is
given).


Format All the Instance Attributes
----------------------------------

The following example prints out every instance attribute. Take note
of how an attribute may be referenced multiple times.

.. code-block:: python
   :linenos:

   In [8]: longer_format = """Formatting attributes for %s
      ...: This instances prefix unit is {unit}, which is a {system} type unit
      ...: The unit value is {value}
      ...: This value can be truncated to just 1 digit of precision: {value:.1f}
      ...: In binary this looks like: {binary}
      ...: The prefix unit is derived from a base of {base}
      ...: Which is raised to the power {power}
      ...: There are {bytes} bytes in this instance
      ...: The instance is {bits} bits large
      ...: bytes/bits without trailing decimals: {bytes:.0f}/{bits:.0f}""" % str(ugly_number)

   In [9]: print ugly_number.format(longer_format)
   Formatting attributes for 5.96046447754MiB
   This instances prefix unit is MiB, which is a NIST type unit
   The unit value is 5.96046447754
   This value can be truncated to just 1 digit of precision: 6.0
   In binary this looks like: 0b10111110101111000010000000
   The prefix unit is derived from a base of 2
   Which is raised to the power 20
   There are 6250000.0 bytes in this instance
   The instance is 50000000.0 bits large
   bytes/bits without trailing decimals: 6250000/50000000

.. note:: On line **4** we print with 1 digit of precision, on line **15** we see the value has been rounded to **6.0**
