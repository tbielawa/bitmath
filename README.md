bitmath
=======

Pythonic module for representing file sizes with different prefix
notations. Created to simplify basic math operations and conversions
when working with file sizes.

**Note** that if seeing 'KiB' or 'GiB' seems strange to you, that's
because we're using the proper NIST Binary Prefixs. Until I add more
docs, you'll just have to look up what that means up online.


Usage
=====

Supported operations:

- Basic arithmetic: addition, subtraction, multiplication, division

- Size comparison: LT, LE, EQ, NE, GT, GE

- Unit conversion: from bytes to exibytes, converstion to any other unit (e.g., Megabytes to Kibibytes)





Quick Examples
==============

Basic unit converstion:

    In [1]: from bitmath import *

    In [2]: fourty_two_mib = MiB(42)

    In [3]: fourty_two_mib_in_kib = fourty_two_mib.to_KiB()

    In [4]: fourty_two_mib_in_kib

    Out[4]: KiB(43008.0)

    In [5]: fourty_two_mib

    Out[5]: MiB(42.0)


Equality testing:

    In [6]: fourty_two_mib == fourty_two_mib_in_kib

    Out[6]: True

Basic math:

    In [7]: eighty_four_mib = fourty_two_mib + fourty_two_mib_in_kib

    In [8]: eighty_four_mib

    Out[8]: MiB(84.0)

    In [9]: eighty_four_mib == fourty_two_mib * 2

    Out[9]: True
