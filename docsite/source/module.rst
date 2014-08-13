.. _module:

.. currentmodule:: bitmath

The ``bitmath`` Module
######################

.. _module_context_managers:

Context Managers
****************

This section describes all of the `context managers
<https://docs.python.org/2/reference/datamodel.html#context-managers>`_
provided by the bitmath class.

To provide a bit of background, a *context manager* (specifically, the
``with`` statement) is a feature of the Python language which is
commonly used to:

* Decorate, or *wrap*, an arbitrary block of code. I.e., effect a
  certain condition onto a specific body of code

* Automatically *open* and *close* an object which is used in a
  specific context. I.e., handle set-up and tear-down of objects in
  the place they are used.

.. seealso::

   :pep:`343`
      *The "with" Statement*

   :pep:`318`
      *Decorators for Functions and Methods*


.. _module_bitmath_format:

bitmath.format()
================

.. function:: bitmath.format([fmt_str=None[, plural=False[, bestprefix=False]]])

   The ``bitmath.format`` context manager allows you to specify the
   string representation of all bitmath instances within a specific
   block of code.

   This is effectively equivalent to applying the
   :ref:`format()<instances_format>` method to an entire region of
   code.

   :param str fmt_str: a formatting mini-language compat formatting
                       string. See the :ref:`instances attributes
                       <instance_attributes>` for a list of available
                       items.
   :param bool plural: ``True`` enables printing instances with
                       trailing **s**'s if they're plural. ``False``
                       (default) prints them as singular (no trailing
                       's')
   :param bool bestprefix: ``True`` enables printing instances in
                           their best human-readable
                           representation. ``False``, the default,
                           prints instances using their current prefix
                           unit.


   .. note:: The ``bestprefix`` parameter is not yet implemented!

   Let's look at an example of toggling pluralization on and off.

   .. code-block:: python
      :linenos:
      :emphasize-lines: 33-34

      import bitmath

      a_single_bit = bitmath.Bit(1)
      technically_plural_bytes = bitmath.Byte(0)
      always_plural_kbs = bitmath.kb(42)

      formatting_args = {
          'not_plural': a_single_bit,
          'technically_plural': technically_plural_bytes,
          'always_plural': always_plural_kbs
      }

      print """None of the following will be pluralized, because that feature is turned off
      """

      test_string = """   One unit of 'Bit': {not_plural}

         0 of a unit is typically said pluralized in US English: {technically_plural}

         several items of a unit will always be pluralized in normal US English
         speech: {always_plural}"""

      print test_string.format(**formatting_args)

      print """
      ----------------------------------------------------------------------
      """

      print """Now, we'll use the bitmath.format() context manager
      to print the same test string, but with pluralization enabled.
      """

      with bitmath.format(plural=True):
          print test_string.format(**formatting_args)

   The context manager is demonstrated in lines **33** → **34**. In
   these lines we use the :py:func:`bitmath.format` context manager,
   setting ``plural`` to ``True``, to print the original string
   again. By doing this we have enabled pluralized string
   representations (where appropriate). Running this script would have
   the following output::


      None of the following will be pluralized, because that feature is turned off

         One unit of 'Bit': 1.0 Bit

         0 of a unit is typically said pluralized in US English: 0.0 Byte

         several items of a unit will always be pluralized in normal US English
         speech: 42.0 kb

      ----------------------------------------------------------------------

      Now, we'll use the bitmath.format() context manager
      to print the same test string, but with pluralization enabled.

         One unit of 'Bit': 1.0 Bit

         0 of a unit is typically said pluralized in US English: 0.0 Bytes

         several items of a unit will always be pluralized in normal US English
         speech: 42.0 kbs

   Here's a shorter example, where we'll:

   * Print a string containing bitmath instances using the default
     formatting (lines **2** → **3**)
   * Use the context manager to print the instances in scientific
     notation (lines **4** → **7**)
   * Print the string one last time to demonstrate how the formatting
     automatically returns to the default format (lines **8** → **9**)

   .. code-block:: python
      :linenos:

      >>> import bitmath
      >>> print "Some instances: %s, %s" % (bitmath.KiB(1 / 3.0), bitmath.Bit(512))
      Some instances: 0.333333333333 KiB, 512.0 Bit
      >>> with bitmath.format("{value:e}-{unit}"):
      ...     print "Some instances: %s, %s" % (bitmath.KiB(1 / 3.0), bitmath.Bit(512))
      ...
      Some instances: 3.333333e-01-KiB, 5.120000e+02-Bit
      >>> print "Some instances: %s, %s" % (bitmath.KiB(1 / 3.0), bitmath.Bit(512))
      Some instances: 0.333333333333 KiB, 512.0 Bit


.. _module_class_variables:

Module Variables
****************

This section describes the module-level variables. Some of which are
constants and are used for reference. Some of which effect output or
behavior.

.. note:: Modifying these variables will change the default
          representation indefinitely. Use the
          :py:func:`bitmath.format` context manager to limit
          changes to a specific block of code.

.. _module_format_string:

.. py:data:: format_string

   This is the default string representation of all bitmath
   instances. The default value is ``{value} {unit}`` which, when
   evaluated, formats an instance as a floating point number with at
   least one digit of precision, followed by a character of
   whitespace, followed by the prefix unit of the instance.

   For example, given bitmath instances representing the following
   values: **1337 MiB**, **0.1234567 kb**, and **0 B**, their printed
   output would look like the following:

   .. code-block:: python

      >>> from bitmath import *
      >>> print MiB(1337), kb(0.1234567), Byte(0)
      1337.0 MiB 0.1234567 kb 0.0 Byte

   We can make these instances print however we want to. Let's wrap
   each one in square brackets (``[``, ``]``), replace the separating
   space character with a hyphen (``-``), and limit the precision to
   just 2 digits:

   .. code-block:: python

      >>> import bitmath
      >>> bitmath.format_string = "[{value:.2f}-{unit}]"
      >>> print bitmath.MiB(1337), bitmath.kb(0.1234567), bitmath.Byte(0)
      [1337.00-MiB] [0.12-kb] [0.00-Byte]

.. py:data:: format_plural

   A boolean which controls the pluralization of instances in string
   representation. The default is ``False``.

   If we wanted to enable pluralization we could set the
   :py:data:`format_plural` variable to ``True``. First, let's look at
   some output using the default singular formatting.

   .. code-block:: python

      >>> import bitmath
      >>> print bitmath.MiB(1337)
      1337.0 MiB

   And now we'll enable pluralization (line **2**):

   .. code-block:: python
      :linenos:
      :emphasize-lines: 2,5

      >>> import bitmath
      >>> bitmath.format_plural = True
      >>> print bitmath.MiB(1337)
      1337.0 MiBs
      >>> bitmath.format_plural = False
      >>> print bitmath.MiB(1337)
      1337.0 MiB

   On line **5** we disable pluralization again and then see that the
   output has no trailing "s" character.
