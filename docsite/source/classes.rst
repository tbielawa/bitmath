.. _classes:

Classes
#######

There are two **fundamental** classes available:

- ``Bit``
- ``Byte``

Available Classes
*****************

There are **24** other classes available, representing all the prefix
units from **k** through **e** (*kilo/kibi* through *exa/exbi*).

Classes with **'i'** in their names are **NIST** type classes. They
were defined by the National Institute of Standards and Technolog
(NIST) as the 'Binary Prefix Units'. They are defined by increasing
powers of 2.

Classes without the **'i'** character are **SI** type classes. Though
not formally defined by any standards organization, they follow the
International System of Units (SI) pattern (commonly used to
abbreviate base 10 values). You may hear these referred to as the
"Decimal" or "SI" prefixes.

Classes ending with *lower-case* **'b'** characters are **bit
based**. Classes ending with upper-case **'B'** characters are **byte
based**. Class inheritance is shown below in parentheses to make this
more apparent:

.. _classes_available:

+---------------+--------------+
| NIST          | SI           |
+===============+==============+
| ``Eib(Bit)``  | ``Eb(Bit)``  |
+---------------+--------------+
| ``EiB(Byte)`` | ``EB(Byte)`` |
+---------------+--------------+
| ``Gib(Bit)``  | ``Gb(Bit)``  |
+---------------+--------------+
| ``GiB(Byte)`` | ``GB(Byte)`` |
+---------------+--------------+
| ``Kib(Bit)``  | ``kb(Bit)``  |
+---------------+--------------+
| ``KiB(Byte)`` | ``kB(Byte)`` |
+---------------+--------------+
| ``Mib(Bit)``  | ``Mb(Bit)``  |
+---------------+--------------+
| ``MiB(Byte)`` | ``MB(Byte)`` |
+---------------+--------------+
| ``Pib(Bit)``  | ``Pb(Bit)``  |
+---------------+--------------+
| ``PiB(Byte)`` | ``PB(Byte)`` |
+---------------+--------------+
| ``Tib(Bit)``  | ``Tb(Bit)``  |
+---------------+--------------+
| ``TiB(Byte)`` | ``TB(Byte)`` |
+---------------+--------------+

**Note**: Yes, as per SI definition, the ``kB`` and ``kb`` classes begins with a lower-case 'k' character.

The majority of the functionality of bitmath object comes from their
rich implementation of standard Python operations. You can use bitmath
objects in **almost all** of the places you would normally use an
integer or a float. See [Usage](#usage) below for more details.

Class Methods
*************

bitmath **class objects** have one public class method which provides
an alternative method to initialize a bitmath class.

- ``BitMathClass.from_other()`` - Instantiate any ``BitMathClass``
  using another instance as reference for it's initial value.

This method may be called on bitmath class objects directly. That is
to say: you do not need to call this method on an instance of a
bitmath class, however that is a valid use case.

**Method Signature:**

.. code-block:: python

   BitMathClass.from_other(bitmath_instance)

The ``from_other()`` class method has one required parameter: an
instance of a bitmath class.
