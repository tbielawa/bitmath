Simple Examples
###############

Basic Bath
**********

**Legend**

**Parameters:** ``bm`` indicates a bitmath object is required in that
position. ``num`` indicates that an integer or decimal value is
required.

+----------------+-------------------+---------------------+-------------------------------------------+
| Operation      | Parameters        | Result Type         | Example                                   |
+================+===================+=====================+===========================================+
| Addition       | ``bm1`` + ``bm2`` | ``type(bm1)``       | ``KiB(1) + KiB(2)`` = ``3.0KiB``          |
+----------------+-------------------+---------------------+-------------------------------------------+
| Addition       | ``bm`` + ``num``  | ``type(num)``       | ``KiB(1) + 1`` = ``2.0``                  |
+----------------+-------------------+---------------------+-------------------------------------------+
| Addition       | ``num`` + ``bm``  | ``type(num)``       | ``1 + KiB(1)`` = ``2.0``                  |
+----------------+-------------------+---------------------+-------------------------------------------+
| Subtraction    | ``bm1`` - ``bm2`` | ``type(bm1)``       | ``KiB(1) - KiB(2)`` = ``-1.0KiB``         |
+----------------+-------------------+---------------------+-------------------------------------------+
| Subtraction    | ``bm`` - ``num``  | ``type(num)``       | ``KiB(4) - 1`` = ``3.0``                  |
+----------------+-------------------+---------------------+-------------------------------------------+
| Subtraction    | ``num`` - ``bm``  | ``type(num)``       | ``10 - KiB(1)`` = ``9.0``                 |
+----------------+-------------------+---------------------+-------------------------------------------+
| Multiplication | ``bm1`` * ``bm2`` | **not implemented** | -                                         |
+----------------+-------------------+---------------------+-------------------------------------------+
| Multiplication | ``bm`` * ``num``  | ``type(bm)``        | ``KiB(2) * 3`` = ``6.0KiB``               |
+----------------+-------------------+---------------------+-------------------------------------------+
| Multiplication | ``num`` * ``bm``  | ``type(num)``       | ``2 * KiB(3)`` = ``6.0``                  |
+----------------+-------------------+---------------------+-------------------------------------------+
| Division       | ``bm1`` / ``bm2`` | ``type(num)``       | ``KiB(1) / KiB(2)`` = ``0.5``             |
+----------------+-------------------+---------------------+-------------------------------------------+
| Division       | ``bm`` / ``num``  | ``type(bm)``        | ``KiB(1) / 3`` = ``0.3330078125KiB``      |
+----------------+-------------------+---------------------+-------------------------------------------+
| Division       | ``num`` / ``bm``  | ``type(num)``       | ``3 / KiB(2)`` = ``1.5``                  |
+----------------+-------------------+---------------------+-------------------------------------------+

Bitwise Operations
******************

Bitwise operations are also supported. Bitwise operations work
directly on the internal ``bits`` attribute of a bitmath instance.

+----------------+-----------------------+---------------------+---------------------------------------------------------+
| Operation      | Parameters            | Result Type         | Example                                                 |
+================+=======================+=====================+=========================================================+
| Left Shift     | ``bm`` << ``num``     | ``type(bm)``        | ``MiB(1)`` << ``2`` = ``MiB(4.0)``                      |
+----------------+-----------------------+---------------------+---------------------------------------------------------+
| Right Shift    | ``bm`` >> ``num``     | ``type(bm)``        | ``MiB(1)`` >> ``2`` = ``MiB(0.25)``                     |
+----------------+-----------------------+---------------------+---------------------------------------------------------+
| AND            | ``bm`` & ``num``      | ``type(bm)``        | ``MiB(13.37)`` & ``1337`` = ``MiB(0.000126...)`` **\*** |
+----------------+-----------------------+---------------------+---------------------------------------------------------+
| OR             | ``bm`` &#124; ``num`` | ``type(bm)``        | ``MiB(13.37)`` &#124; ``1337`` = ``MiB(13.3700...)``    |
+----------------+-----------------------+---------------------+---------------------------------------------------------+
| XOR            | ``bm`` ^ ``num``      | ``type(bm)``        | ``MiB(13.37)`` ^ ``1337`` = ``MiB(13.369...)``          |
+----------------+-----------------------+---------------------+---------------------------------------------------------+

**\*** - _Give me a break here, it's not easy coming up with compelling examples for bitwise operations..._


Other Features
**************

- Size comparison: LT, LE, EQ, NE, GT, GE

- Unit conversion: from bytes through exibytes, supports conversion to any other unit (e.g., Megabytes to Kibibytes)


Examples
********

Basic unit conversion:


.. code-block:: python

   In [1]: from bitmath import *

   In [2]: fourty_two_mib = MiB(42)

   In [3]: fourty_two_mib_in_kib = fourty_two_mib.to_KiB()

   In [4]: fourty_two_mib_in_kib

   Out[4]: KiB(43008.0)

   In [5]: fourty_two_mib

   Out[5]: MiB(42.0)


Equality testing:

.. code-block:: python

   In [6]: fourty_two_mib == fourty_two_mib_in_kib

   Out[6]: True

Basic math:

.. code-block:: python

   In [7]: eighty_four_mib = fourty_two_mib + fourty_two_mib_in_kib

   In [8]: eighty_four_mib

   Out[8]: MiB(84.0)

   In [9]: eighty_four_mib == fourty_two_mib * 2

   Out[9]: True


Sorting is also supported:

.. code-block:: python

   In [1]: from bitmath import *

   In [2]: import os

   In [3]: sizes = []

   In [4]: for f in os.listdir('./tests/'):
               sizes.append(KiB(os.path.getsize('./tests/' + f)))

   In [5]: print sizes
   [KiB(7337.0), KiB(1441.0), KiB(2126.0), KiB(2178.0), KiB(2326.0), KiB(4003.0), KiB(48.0), KiB(1770.0), KiB(7892.0), KiB(4190.0)]

   In [6]: print sorted(sizes)
   [KiB(48.0), KiB(1441.0), KiB(1770.0), KiB(2126.0), KiB(2178.0), KiB(2326.0), KiB(4003.0), KiB(4190.0), KiB(7337.0), KiB(7892.0)]
