Instances
#########

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
representation. All of the instances attributes (next section) are
available to use when choosing a representation.

The following are some examples of how to use the ``format`` method:




Instance Attributes
*******************

bitmath objects have a few public instance attributes:

- ``bytes`` - The number of bytes in the object
- ``bits`` - The number of bits in the object
- ``value`` - The value of the instance in **PREFIX** units
- ``binary`` - The `Python binary representation <https://docs.python.org/2/library/functions.html#bin>`_ of the instance's value (in bits). ``bin`` is an alias for ``binary``

For example:

.. code-block:: python

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
