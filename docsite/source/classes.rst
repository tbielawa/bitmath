.. _classes:

Classes
#######

.. contents::
   :depth: 3
   :local:

Initializing
************

API signature:

.. code-block:: python

   BitMathType([value=0, [bytes=None, [bits=None]]])

A bitmath type may be initialized in four different ways:

No initial value
================

The default size is 0

.. code-block:: python

   zero_kib = KiB()

Set The Value In Prefix Units
=============================

That is to say, if you want to encapsulate **1KiB**, initialize the
bitmath type with ``1``:

.. code-block:: python

   one_kib = KiB(1)

   one_kib = KiB(value=1)


Set The Number Of Bytes
=======================

Use the ``bytes`` keyword

.. code-block:: python

   one_kib = KiB(bytes=1024)


Set The Number Of Bits
======================

Use the ``bits`` keyword

.. code-block:: python

   one_kib = KiB(bits=8192)



Available Classes
*****************

There are two **fundamental** classes available, the ``Bit`` and the
``Byte``.

There are **24** other classes available, representing all the prefix
units from **k** through **e** (*kilo/kibi* through *exa/exbi*).

Classes with **'i'** in their names are **NIST** type classes. They
were defined by the `National Institute of Standards and Technology
(NIST) <http://www.nist.gov/>`_ as the 'Binary Prefix Units'. They are
defined by increasing powers of 2.

Classes without the **'i'** character are **SI** type classes. Though
not formally defined by any standards organization, they follow the
`International System of Units (SI) <http://www.bipm.org/en/si/>`_
pattern (commonly used to abbreviate base 10 values). You may hear
these referred to as the "Decimal" or "SI" prefixes.

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

.. note:: As per SI definition, the ``kB`` and ``kb`` classes begins
          with a *lower-case* **k** character.

The majority of the functionality of bitmath object comes from their
rich implementation of standard Python operations. You can use bitmath
objects in **almost all** of the places you would normally use an
integer or a float. See the :ref:`Table of Supported Operations
<simple_examples_supported_operations>` and :ref:`Appendix: Rules for
Math <appendix_math>` for more details.

Class Methods
*************

bitmath **class objects** have one public class method which provides
an alternative way to initialize a bitmath class.

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

In pure Python, this could also be written as:

.. code-block:: python
   :linenos:
   :emphasize-lines: 3

   In [1]: a_mebibyte = MiB(1)

   In [2]: a_mebibyte_sized_kibibyte = KiB(bytes=a_mebibyte.bytes)

   In [3]: a_mebibyte == a_mebibyte_sized_kibibyte
   Out[3]: True

   In [4]: print a_mebibyte, a_mebibyte_sized_kibibyte
   1.0MiB 1024.0KiB
