Simple Examples
###############

**Legend**

* ``bm`` indicates a bitmath object is required
* ``num`` indicates that an integer or decimal value is required

Basic Bath
**********

Math works mostly like you expect it to, except for the special cases
where: we mix bitmath types with Number types, and operations where
two bitmath types would cancel out (such as dividing two bitmath
types).

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
| Multiplication | ``bm1`` * ``bm2`` | ✕                   | ✕                                         |
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
directly on the ``bits`` attribute of a bitmath instance, not the
number you see in an instances printed representation (``value``), to
maintain accuracy.

+----------------+-----------------------+--------------+---------------------------------------------------------+
| Operation      | Parameters            | Result Type  | Example ¹                                               |
+================+=======================+==============+=========================================================+
| Left Shift     | ``bm`` << ``num``     | ``type(bm)`` | ``MiB(1)`` << ``2`` = ``MiB(4.0)``                      |
+----------------+-----------------------+--------------+---------------------------------------------------------+
| Right Shift    | ``bm`` >> ``num``     | ``type(bm)`` | ``MiB(1)`` >> ``2`` = ``MiB(0.25)``                     |
+----------------+-----------------------+--------------+---------------------------------------------------------+
| AND            | ``bm`` & ``num``      | ``type(bm)`` | ``MiB(13.37)`` & ``1337`` = ``MiB(0.000126...)``        |
+----------------+-----------------------+--------------+---------------------------------------------------------+
| OR             | ``bm`` \|     ``num`` | ``type(bm)`` | ``MiB(13.37)`` \|     ``1337`` = ``MiB(13.3700...)``    |
+----------------+-----------------------+--------------+---------------------------------------------------------+
| XOR            | ``bm`` ^ ``num``      | ``type(bm)`` | ``MiB(13.37)`` ^ ``1337`` = ``MiB(13.369...)``          |
+----------------+-----------------------+--------------+---------------------------------------------------------+

¹ - *Give me a break here, it's not easy coming up with compelling examples for bitwise operations...*


Other Features
**************

- Size comparison: ``<``, ``≤``, ``==``, ``≠``, ``>``, ``≥``

- Unit conversion: from bytes through exibytes, supports conversion to any other unit (e.g., Megabytes to Kibibytes)


Examples
********

Basic unit conversion:


.. code-block:: python
   :linenos:

   In [1]: from bitmath import *

   In [2]: fourty_two_mib = MiB(42)

   In [3]: fourty_two_mib_in_kib = fourty_two_mib.to_KiB()

   In [4]: fourty_two_mib_in_kib

   Out[4]: KiB(43008.0)

   In [5]: fourty_two_mib

   Out[5]: MiB(42.0)


Equality testing:

.. code-block:: python
   :linenos:

   In [6]: fourty_two_mib == fourty_two_mib_in_kib

   Out[6]: True

Basic math:

.. code-block:: python
   :linenos:

   In [7]: eighty_four_mib = fourty_two_mib + fourty_two_mib_in_kib

   In [8]: eighty_four_mib

   Out[8]: MiB(84.0)

   In [9]: eighty_four_mib == fourty_two_mib * 2

   Out[9]: True


Sorting is also supported:

.. code-block:: python
   :linenos:

   In [1]: from bitmath import *

   In [2]: import os

   In [3]: sizes = []

   In [4]: for f in os.listdir('./tests/'):
               sizes.append(KiB(os.path.getsize('./tests/' + f)))

   In [5]: print sizes
   [KiB(7337.0), KiB(1441.0), KiB(2126.0), KiB(2178.0), KiB(2326.0), KiB(4003.0), KiB(48.0), KiB(1770.0), KiB(7892.0), KiB(4190.0)]

   In [6]: print sorted(sizes)
   [KiB(48.0), KiB(1441.0), KiB(1770.0), KiB(2126.0), KiB(2178.0), KiB(2326.0), KiB(4003.0), KiB(4190.0), KiB(7337.0), KiB(7892.0)]

   In [7]: human_sizes = [s.best_prefix() for s in sizes]

   In [8]: print sorted(human_sizes)
   [KiB(48.0), MiB(1.4072265625), MiB(1.728515625), MiB(2.076171875), MiB(2.126953125), MiB(2.271484375), MiB(3.9091796875), MiB(4.091796875), MiB(7.1650390625), MiB(7.70703125)]
