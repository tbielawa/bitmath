bitmath
=======

Represents file sizes with different prefix notations. Created to
simplify basic math operations and conversions in a Pythonic
way. Supports SI and NIST binary prefixes.

In discussion we will refer to the NIST units primarily. I.e., instead
of "megabyte" we will refer to "mibibyte". The former is 10^3 =
1,000,000 bytes, whereas the second is 2^20 = 1,048,576 bytes. When
you see file sizes in your file browser, or transfer rates in your web
browser, what you're really seeing are the base-2 sizes/rates.


Classes
=======

- Byte

**NIST**

- KiB
- MiB
- GiB
- TiB
- PiB
- EiB

**SI**

- kB
- MB
- GB
- TB
- PB
- EB

**Note**: Yes, as per SI definition, the ``kB`` class begins with a lower-case 'k' character.


Usage
=====

Supported operations:

- Basic arithmetic: addition, subtraction, multiplication, division

- Size comparison: LT, LE, EQ, NE, GT, GE

- Unit conversion: from bytes to exibytes, supports conversion to any other unit (e.g., Megabytes to Kibibytes)


Instantiating any bitmath type is simple:

    one_kib = KiB(1)
    KiB(1.0)

Likewise, if you want to represent the same thing in bytes:

    one_kib_as_byte = Byte(1024)
    Byte(1024.0)

In these examples ``one_kib`` and ``one_kib_as_byte`` are equivalent
if tested with the ``==`` operator.


See **Quick Examples** for more examples of supported operations.


Examples
========

Basic unit conversion:

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


Real Life Examples
==================

**Example 1: Download Speeds**

Let's pretend that your Internet service provider (ISP) advertises
your maximum downstream as **50Mbps** [1] and you want to know how
fast that is in mibibytes? ``bitmath`` can do that for you
easily. Keeping in mind that 1 Byte = 8 bits you can calculate this as
such:

    from bitmath import *

    downstream = MB(50)

    downstream.to_MiB() / 8

    MiB(5.96046447754)

This tells us that if our ISP advertises **50Mbps** we can expect to
see download rates of nearly **6MiB/sec**.

**[1]** - Assuming your ISP follows the common industry practice of
  using SI (base-10) units to describe file sizes/rates.

**Example 2: Calculating how many files fit on a device**

Given that we have a thumb drive with 12GiB free, how many 4MiB audio
files can we fit on it?


    from bitmath import *

    thumb_drive = GiB(12)

    audio_file = MiB(4)

    thumb_drive / audio_file

    3072.0

This tells us that we could fit 3072 4MiB audio files on a 12GiB thumb drive.


**Example 3: Printing Human-Readable File Sizes in Python**

In a Python script or intrepreter we may wish to print out file sizes
in something other than bytes (which is what ``os.path.getsize``
returns). We can use ``bitmath`` to do that too:


    >>> import os

    >>> from bitmath import *

    >>> these_files = os.listdir('.')

    >>> for f in these_files:
            f_size = Byte(os.path.getsize(f))
            print "%s - %s" % (f, f_size.to_KiB())

    test_basic_math.py - 3.048828125KiB
    __init__.py - 0.1181640625KiB
    test_representation.py - 0.744140625KiB
    test_to_Type_conversion.py - 2.2119140625KiB


On Units
========

In this module you will find two very similar sets of classes
available. These are the **NIST** and **SI** prefixes. The **NIST**
prefixes are all base 2 and have an 'i' character in the middle. The
**SI** prefixes are base 10 and have no 'i' character.

Why? The Linux Documentation Project says the following:

    Before these binary prefixes were introduced, it was fairly common to use k=1000 and K=1024, just like b=bit, B=byte.  Unfortunately, the M is capital already, and cannot be capitalized to indicate binary-ness.

    At first that didn't matter too much, since memory modules and disks came in sizes that were powers of two, so everyone knew that in such contexts "kilobyte" and "megabyte" meant 1024 and 1048576 bytes, respectively.  What originally was a sloppy use of the prefixes "kilo" and "mega" started to become regarded as the "real true meaning" when computers were involved.  But then disk technology changed, and disk sizes became arbitrary numbers.  After a period of uncertainty all disk manufacturers settled on the standard, namely k=1000, M=1000k, G=1000M.

    The situation was messy: in the 14k4 modems, k=1000; in the 1.44MB diskettes, M=1024000; etc.  In 1998 the IEC approved the standard that defines the binary prefixes given above, enabling people to be precise and unambiguous.

    Thus, today, MB = 1000000B and MiB = 1048576B.

    In the free software world programs are slowly being changed to conform.  When the Linux kernel boots and says

        hda: 120064896 sectors (61473 MB) w/2048KiB Cache

    the MB are megabytes and the KiB are kibibytes.

Furthermore, to quote the National Institute of Standards and Technology:

    "Once upon a time, computer professionals noticed that 210 was very nearly equal to 1000 and started using the SI prefix "kilo" to mean 1024. That worked well enough for a decade or two because everybody who talked kilobytes knew that the term implied 1024 bytes. But, almost overnight a much more numerous "everybody" bought computers, and the trade computer professionals needed to talk to physicists and engineers and even to ordinary people, most of whom know that a kilometer is 1000 meters and a kilogram is 1000 grams.

    "Then data storage for gigabytes, and even terabytes, became practical, and the storage devices were not constructed on binary trees, which meant that, for many practical purposes, binary arithmetic was less convenient than decimal arithmetic. The result is that today "everybody" does not "know" what a megabyte is. When discussing computer memory, most manufacturers use megabyte to mean 220 = 1 048 576 bytes, but the manufacturers of computer storage devices usually use the term to mean 1 000 000 bytes. Some designers of local area networks have used megabit per second to mean 1 048 576 bit/s, but all telecommunications engineers use it to mean 106 bit/s. And if two definitions of the megabyte are not enough, a third megabyte of 1 024 000 bytes is the megabyte used to format the familiar 90 mm (3 1/2 inch), "1.44 MB" diskette. The confusion is real, as is the potential for incompatibility in standards and in implemented systems.

    "Faced with this reality, the IEEE Standards Board decided that IEEE standards will use the conventional, internationally adopted, definitions of the SI prefixes. Mega will mean 1 000 000, except that the base-two definition may be used (if such usage is explicitly pointed out on a case-by-case basis) until such time that prefixes for binary multiples are adopted by an appropriate standards body."

Source: http://physics.nist.gov/cuu/Units/prefixes.html

You may also be interested in ``man 7 units``: http://man7.org/linux/man-pages/man7/units.7.html
