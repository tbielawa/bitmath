
[![Build Status](https://api.travis-ci.org/tbielawa/bitmath.png)](https://travis-ci.org/tbielawa/bitmath/)
[![Coverage Status](https://img.shields.io/coveralls/tbielawa/bitmath.svg)](https://coveralls.io/r/tbielawa/bitmath?branch=master)
[![Documentation](https://readthedocs.org/projects/bitmath/badge/?version=latest)](https://readthedocs.org/projects/bitmath/?badge=latest)


bitmath
=======
*bitmath* simplifies many facets of interacting with file sizes in
various units. Functionality includes:

* Converting between **SI** and **NIST** prefix units (``GiB`` to ``kB``)
* Converting between units of the same type (SI to SI, or NIST to NIST)
* Basic arithmetic operations (subtracting 42KiB from 50GiB)
* Rich comparison operations (``1024 Bytes == 1KiB``)
* bitwise operations (``<<``, ``>>``, ``&``, ``|``, ``^``)
* Sorting
* Automatic human-readable prefix selection (like in [hurry.filesize](https://pypi.python.org/pypi/hurry.filesize))

In addition to the conversion and math operations, `bitmath` provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications. The
format produced for these representations is customizable via the
functionality included in stdlibs
[string.format](https://docs.python.org/2/library/string.html).

In discussion we will refer to the NIST units primarily. I.e., instead
of "megabyte" we will refer to "mebibyte". The former is ``10^3 =
1,000,000`` bytes, whereas the second is ``2^20 = 1,048,576``
bytes. When you see file sizes or transfer rates in your web browser,
most of the time what you're really seeing are the base-2 sizes/rates.

OH! And did we mention it has 150+ unittests? [Check them out for
yourself](https://github.com/tbielawa/bitmath/tree/master/tests]).


Documentation
=============

The main documentation has been moved to
[http://bitmath.readthedocs.org/en/latest/](http://bitmath.readthedocs.org/en/latest/).

Topics include:

* The `bitmath` Module
  * Functions
  * Context Managers
  * Module Variables
* Classes
  * Initializing
  * Available Classes
  * Class Methods
* Instances
  * Instance Attributes
  * Instance Methods
  * Instance Properties
  * The Formatting Mini-Language
* Getting Started
  * Tables of Supported Operations
  * Basic Math
  * Unit Conversion
  * Rich Comparison
  * Sorting
* Real Life Examples
  * Download Speeds
  * Calculating how many files fit on a device
  * Printing Human-Readable File Sizes in Python
  * Calculating Linux BDP and TCP Window Scaling
* Contributing to bitmath
* Appendices
  * Rules for Math
  * On Units
* Copyright


Examples
========

What good would a README be without examples?

## Arithmetic

    In [1]: from bitmath import *

    In [2]: log_size = kB(137.4)

    In [3]: log_zipped_size = Byte(987)

    In [4]: print "Compression saved %s space" % (log_size - log_zipped_size)
    Compression saved 136.413kB space

    In [5]: thumb_drive = GiB(12)

    In [6]: song_size = MiB(5)

    In [7]: songs_per_drive = thumb_drive / song_size

    In [8]: print songs_per_drive
    2457.6

## Convert Units
### With to method
    In [1]: from bitmath import *

    In [2]: dvd_size = GiB(4.7)

    In [3]: print "DVD Size in MiB: %s" % dvd_size.to_MiB()
    DVD Size in MiB: 4812.8MiB

### With Properties
    In [1]: from bitmath import *

    In [2]: dvd_size = GiB(4.7)

    In [3]: print "DVD Size in MiB: %s" % dvd_size.MiB
    DVD Size in MiB: 4812.8MiB


## Select a human-readable unit

    In [4]: small_number = kB(100)

    In [5]: ugly_number = small_number.TiB

    In [6]: print ugly_number
    9.09494701773e-08TiB

    In [7]: print ugly_number.best_prefix()
    97.65625KiB


## Rich Comparison

    In [8]: cd_size = MiB(700)

    In [9]: cd_size > dvd_size
    Out[9]: False

    In [10]: cd_size < dvd_size
    Out[10]: True

    In [11]: MiB(1) == KiB(1024)
    Out[11]: True

    In [12]: MiB(1) <= KiB(1024)
    Out[12]: True

## Sorting

    In [13]: sizes = [KiB(7337.0), KiB(1441.0), KiB(2126.0), KiB(2178.0),
                      KiB(2326.0), KiB(4003.0), KiB(48.0), KiB(1770.0),
                      KiB(7892.0), KiB(4190.0)]

    In [14]: print sorted(sizes)
    [KiB(48.0), KiB(1441.0), KiB(1770.0), KiB(2126.0), KiB(2178.0),
    KiB(2326.0), KiB(4003.0), KiB(4190.0), KiB(7337.0), KiB(7892.0)]

## Custom Formatting

* Use of the custom formatting system
* All of the available instance properties

Example:

    In [8]: longer_format = """Formatting attributes for %s
       ...: This instances prefix unit is {unit}, which is a {system} type unit
       ...: The unit value is {value}
       ...: This value can be truncated to just 1 digit of precision: {value:.1f}
       ...: This value can be truncated to just 2 significant digits: {value:.2g}
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

## Utility Functions

**bitmath.getsize()**

    >>> print bitmath.getsize('python-bitmath.spec')
    3.7060546875 KiB

**bitmath.parse_string()**

    >>> import bitmath
    >>> a_dvd = bitmath.parse_string("4.7 GiB")
    >>> print type(a_dvd)
    <class 'bitmath.GiB'>
    >>> print a_dvd
    4.7 GiB

**bitmath.listdir()**

    >>> for i in bitmath.listdir('./tests/', followlinks=True, relpath=True, bestprefix=True):
    ...     print i
    ...
    ('tests/test_file_size.py', KiB(9.2900390625))
    ('tests/test_basic_math.py', KiB(7.1767578125))
    ('tests/__init__.py', KiB(1.974609375))
    ('tests/test_bitwise_operations.py', KiB(2.6376953125))
    ('tests/test_context_manager.py', KiB(3.7744140625))
    ('tests/test_representation.py', KiB(5.2568359375))
    ('tests/test_properties.py', KiB(2.03125))
    ('tests/test_instantiating.py', KiB(3.4580078125))
    ('tests/test_future_math.py', KiB(2.2001953125))
    ('tests/test_best_prefix_BASE.py', KiB(2.1044921875))
    ('tests/test_rich_comparison.py', KiB(3.9423828125))
    ('tests/test_best_prefix_NIST.py', KiB(5.431640625))
    ('tests/test_unique_testcase_names.sh', Byte(311.0))
    ('tests/.coverage', KiB(3.1708984375))
    ('tests/test_best_prefix_SI.py', KiB(5.34375))
    ('tests/test_to_built_in_conversion.py', KiB(1.798828125))
    ('tests/test_to_Type_conversion.py', KiB(8.0185546875))
    ('tests/test_sorting.py', KiB(4.2197265625))
    ('tests/listdir_symlinks/10_byte_file_link', Byte(10.0))
    ('tests/listdir_symlinks/depth1/depth2/10_byte_file', Byte(10.0))
    ('tests/listdir_nosymlinks/depth1/depth2/10_byte_file', Byte(10.0))
    ('tests/listdir_nosymlinks/depth1/depth2/1024_byte_file', KiB(1.0))
    ('tests/file_sizes/kbytes.test', KiB(1.0))
    ('tests/file_sizes/bytes.test', Byte(38.0))
    ('tests/listdir/10_byte_file', Byte(10.0))

## Formatting

    >> with bitmath.format(fmt_str="[{value:.3f}@{unit}]"):
    ...     for i in bitmath.listdir('./tests/', followlinks=True, relpath=True, bestprefix=True):
    ...         print i[1]
    ...
    [9.290@KiB]
    [7.177@KiB]
    [1.975@KiB]
    [2.638@KiB]
    [3.774@KiB]
    [5.257@KiB]
    [2.031@KiB]
    [3.458@KiB]
    [2.200@KiB]
    [2.104@KiB]
    [3.942@KiB]
    [5.432@KiB]
    [311.000@Byte]
    [3.171@KiB]
    [5.344@KiB]
    [1.799@KiB]
    [8.019@KiB]
    [4.220@KiB]
    [10.000@Byte]
    [10.000@Byte]
    [10.000@Byte]
    [1.000@KiB]
    [1.000@KiB]
    [38.000@Byte]
    [10.000@Byte]
