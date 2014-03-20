bitmath
=======

bitmath simplifies many facets of interacting with file sizes in
various units. Examples include: converting between SI and NIST prefix
units (GiB to kB), converting between units of the same type (SI to
SI, or NIST to NIST), basic arithmetic operations (subtracting 42KiB
from 50GiB), and rich comparison operations (1024 Bytes == 1KiB).

In addition to the conversion and math operations, bitmath provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications.

In discussion we will refer to the NIST units primarily. I.e., instead
of "megabyte" we will refer to "mibibyte". The former is 10^3 =
1,000,000 bytes, whereas the second is 2^20 = 1,048,576 bytes. When
you see file sizes in your file browser, or transfer rates in your web
browser, what you're really seeing are the base-2 sizes/rates.


Basics
======

### Class Initializer Signature

    BitMathType([value=0, [bytes=None, [bits=None]]])

A bitmath type may be initialized in four different ways:

- Set no initial value

The default size is 0

    zero_kib = KiB()

- Set the value **in current prefix units**

That is to say, if you want to encapsulate 1KiB, initialize the
bitmath type with ``1``:

    one_kib = KiB(1)

	one_kib = KiB(value=1)

- Set the number of bytes

Use the ``bytes`` keyword

    one_kib = KiB(bytes=1024)

- Set the number of bits

Use the ``bits`` keyword

    one_kib = KiB(bits=8192)

### Class Methods

bitmath **class objects** have one public class method which provides
an alternative method to initialize a bitmath class.

- ``BitMathClass.from_other()`` - Instantiate any ``BitMathClass``
  using another instance as reference for it's initial value.

This method may be called on bitmath class objects directly. That is
to say: you do not need to call this method on an instance of a
bitmath class, however that is a valid use case.

**Method Signature:**

    BitMathClass.from_other(bitmath_instance)

The ``from_other()`` class method has one required parameter: an
instance of a bitmath class.



Available Classes
-----------------

There are two **fundamental** classes available:

- ``Bit``
- ``Byte``

There are 24 other classes available, representing all the prefix
units from "k" through "e" (kilo/kibi through exa/exbi).

Classes with 'i' in their names are **NIST** type classes. They were
defined by the National Institute of Standards and Technolog (NIST) as
the 'Binary Prefix Units'. They are defined by increasing powers of 2.

Classes without the 'i' character are **SI** type classes. Though not
formally defined by any standards organization, they follow the
International System of Units (SI) pattern (commonly used to
abbreviate base 10 values). You may hear these referred to as the
"Decimal" or "SI" prefixes.

Classes ending with lower-case 'b' characters are **bit
based**. Classes ending with upper-case 'B' characters are **byte
based**. Class inheritance is shown below in parentheses to make this
more apparent:

- ``Eb(Bit)``
- ``EB(Byte)``
- ``Eib(Bit)``
- ``EiB(Byte)``
- ``Gb(Bit)``
- ``GB(Byte)``
- ``Gib(Bit)``
- ``GiB(Byte)``
- ``kb(Bit)``
- ``kB(Byte)``
- ``Kib(Bit)``
- ``KiB(Byte)``
- ``Mb(Bit)``
- ``MB(Byte)``
- ``Mib(Bit)``
- ``MiB(Byte)``
- ``Pb(Bit)``
- ``PB(Byte)``
- ``Pib(Bit)``
- ``PiB(Byte)``
- ``Tb(Bit)``
- ``TB(Byte)``
- ``Tib(Bit)``
- ``TiB(Byte)``

**Note**: Yes, as per SI definition, the ``kB`` and ``kb`` classes begins with a lower-case 'k' character.

The majority of the functionality of bitmath object comes from their
rich implementation of standard Python operations. You can use bitmath
objects in **almost all** of the places you would normally use an
integer or a float. See **Usage** below for more details.


Instance Methods
----------------

bitmath objects come with one basic method: ``to_THING()``.

Where ``THING`` is any of the bitmath types. You can even
``to_THING()`` an instance into itself again:

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


Instance Attributes
-------------------

bitmath objects have three public instance attributes:

- ``bytes`` - The number of bytes in the object
- ``bits`` - The number of bits in the object
- ``value`` - The value of the instance in **PREFIX** units

For example:

    In [13]: dvd_capacity = GB(4.7)

    In [14]: print "Capacity in bits: %s\nbytes: %s\n" % \

                 (dvd_capacity.bits, dvd_capacity.bytes)

       Capacity in bits: 37600000000.0

       bytes: 4700000000.0

    In [15]: dvd_capacity.value

    Out[16]: 4.7


Usage
=====

Supported operations:

- Basic arithmetic: addition, subtraction, multiplication, division

Math works mostly like you expect it to, except for the special cases
where we mix bitmath types with Number types, and operations where two
bitmath types would cancel out (like such as dividing two bitmath
types)

**Legend**

- **Parameters:** ``bm`` indicates a bitmath object is required
in that position. ``num`` indicates that an integer or decimal value
is required.

| Operation      | Parameters        | Result Type         | Example                                   |
| ---------------|-------------------|---------------------|-------------------------------------------|
| Addition       | ``bm1`` + ``bm2`` | ``type(bm1)``       | ``KiB(1) + KiB(2)`` = ``3.0KiB``          |
| Addition       | ``bm`` + ``num``  | ``type(num)``       | ``KiB(1) + 1`` = ``2.0``                  |
| Addition       | ``num`` + ``bm``  | ``type(num)``       | ``1 + KiB(1)`` = ``2.0``                  |
| Subtraction    | ``bm1`` - ``bm2`` | ``type(bm1)``       | ``KiB(1) - KiB(2)`` = ``-1.0KiB``         |
| Subtraction    | ``bm`` - ``num``  | ``type(num)``       | ``KiB(4) - 1`` = ``3.0``                  |
| Subtraction    | ``num`` - ``bm``  | ``type(num)``       | ``10 - KiB(1)`` = ``9.0``                 |
| Multiplication | ``bm1`` * ``bm2`` | **not implemented** | -                                         |
| Multiplication | ``bm`` * ``num``  | ``type(bm)``        | ``KiB(2) * 3`` = ``6.0KiB``               |
| Multiplication | ``num`` * ``bm``  | ``type(num)``       | ``2 * KiB(3)`` = ``6.0``                  |
| Division       | ``bm1`` / ``bm2`` | ``type(num)``       | ``KiB(1) / KiB(2)`` = ``0.5``             |
| Division       | ``bm`` / ``num``  | ``type(bm)``        | ``KiB(1) / 3`` = ``0.3330078125KiB``      |
| Division       | ``num`` / ``bm``  | ``type(num)``       | ``3 / KiB(2)`` = ``1.5``                  |


- Size comparison: LT, LE, EQ, NE, GT, GE

- Unit conversion: from bytes through exibytes, supports conversion to any other unit (e.g., Megabytes to Kibibytes)


Instantiating any bitmath type is simple:

    one_kib = KiB(1)
    KiB(1.0)

Likewise, if you want to represent the same thing in bytes:

    one_kib_as_byte = Byte(1024)
    Byte(1024.0)

In these examples ``one_kib`` and ``one_kib_as_byte`` are equivalent
if tested with the ``==`` operator.


See **Examples** for more examples of supported operations.


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


**Example 4: Calculating Linux BDP and TCP Window Scaling**

Say we're doing some Linux Kernel TCP performance tuning. For optimum
speeds we need to calculate our BDP, or Bandwidth Delay Product. For
this we need to calculate certain values to set some kernel tuning
parameters to. The point of this tuning is to send the most data we
can during a measured round-trip-time without sending more than can be
processed. To accomplish this we are resizing our kernel read/write
networking/socket buffers.

**Core Networking Values**

- ``net.core.rmem_max`` - **Bytes** - Single Value - Default receive buffer size
- ``net.core.wmem_max`` - **Bytes** - Single Value - Default write buffer size

**System-Wide Memory Limits**

- ``net.ipv4.tcp_mem`` - **Pages** - Three Value Vector - The ``max`` field of the parameter is the number of **memory pages** allowed for queueing by all TCP sockets.

**Per-Socket Buffers**

Per-socket buffer sizes must not exceede the core networking buffer sizes.

- ``net.ipv4.tcp_rmem`` - **Bytes** - Three Field Vector - The ``max`` field sets the size of the TCP receive buffer
- ``net.ipv4.tcp_wmem`` - **Bytes** - Three Field Vector - As above, but for the write buffer

We would normally calculate the optimal BDP and related values following this approach:

1. Measure the latency, or round trip time (RTT), between the host we're tuning and our target remote host
1. Measure/identify our network transfer rate
1. Calculate the BDP (multiply transfer rate by rtt)
1. Obtain our current kernel settings
1. Adjust settings as necessary

But for the sake brevity we'll be working out of an example scenario
with a pre-defined RTT and transfer rate.

**Scenario**

- We have an average network transfer rate of 1Gb/sec (where ``Gb`` is the SI unit for Gigabits, not Gibibytes)
- Our latency (RTT) is 0.199ms (milliseconds)

**Calculate Manually**

Lets calculate the BDP now. Because the kernel parameters expect
values in units of bytes and pages we'll have to convert our transfer
rate of 1Gb/sec into B/s (Gigabits/second to Bytes/second):

- Convert 1Gb into an equivalent **byte** based unit

Remember 1 Byte = 8 Bytes:

    tx_rate_GB = 1/8 = 0.125

Our equivalent transfer rate is 0.125GB/sec.

- Convert our RTT from miliseconds into seconds

Remember 1ms = 10^-3s:

    window_seconds = 0.199 * 10^-3 = 0.000199

Our equivalent RTT window is 0.000199s

- Next we multiply the transfer rate by the length of our RTT window (in seconds)

(The unit analysis for this is ``GB/s * s`` leaving us with ``GB``)

    BDP = rx_rate_GB * window_seconds = 0.125 * 0.000199 = 0.000024875

Our BDP is 0.000024875GB.

- Convert 0.000024875GB to bytes:

Remember 1GB = 10^9B

    BDP_bytes = 0.000024875 * 10^9 = 24875.0

Our BDP is 24875 bytes (or about 24.3KiB)

**Calculate with bitmath**

All of this math can be done much quicker (and with greater accuracy)
using the bitmath library. Let's see how:

    from bitmath import GB

    tx = 1/8.0

    rtt = 0.199 * 10**-3

    bdp = (GB(tx * rtt)).to_Byte()

    Byte(24875.0)

    bdp.to_KiB()

    KiB(24.2919921875)

**Note:** To avoid integer rounding during division, don't forget to divide by ``8.0`` rather than ``8``

We could shorten that even further:

    print (GB((1/8.0) * (0.199 * 10**-3))).to_Byte()

	24875.0Byte

**Get the current kernel parameters**

Important to note is that the **per-socket** buffer sizes must not
exceed the **core network** buffer sizes. Lets fetch our current core
buffer sizes:

    $ sysctl net.core.rmem_max net.core.wmem_max

    net.core.rmem_max = 212992

    net.core.wmem_max = 212992

Recall, these values are in bytes. What are they in KiB?

    Byte(212992).to_KiB()

    KiB(208.0)

This means our core networking buffer sizes are set to 208KiB
each. Now let's check our current per-socket buffer sizes:

    $ sysctl net.ipv4.tcp_rmem net.ipv4.tcp_wmem

    net.ipv4.tcp_rmem = 4096        87380   6291456

    net.ipv4.tcp_wmem = 4096        16384   4194304

Let's double-check that our buffer sizes aren't already out of wack
(per-socket should be <= networking core)

    net_core_max = KiB(bytes=212992)

    ipv4_tcp_rmem_max = KiB(bytes=6291456)

    ipv4_tcp_rmem_max > net_core_max

    True

It appears that my buffers aren't sized appropriately. We'll fix that
when we set the tunable parameters.

Finally, how large is the entire system TCP buffer?

    $ sysctl net.ipv4.tcp_mem

    net.ipv4.tcp_mem = 280632       374176  561264

Our max system TCP buffer size is set to **561264**. Recall that this
parameter is measured in **memory pages**. Most of the time your page
size is ``4096 bytes``, but you can check by running the command:
``getconf PAGESIZE``. To convert the system TCP buffer size
(561264) into a byte-based unit, we'll multiply it by our pagesize
(4096):

    sys_pages = 561264

    page_size = 4096

    sys_buffer = Byte(sys_pages * page_size)

    print sys_buffer.to_MiB()

    2192.4375MiB

    print sys_buffer.to_GiB()

    2.14105224609GiB

The system max TCP buffer size is about 2.14GiB.

In review, we discovered the following:

* Our **core network** buffer size is insufficient (**212992**), we'll set it higher
* Our current **per-socket** buffer sizes are **6291456** and **4194304**

And we calculated the following:

* Our ideal **max** per-socket buffer size is **24875** bytes
* Our ideal **default** per-socket buffer size (half the **max**): **12437**


**Finally: Set the new kernel parameters**

Set the **core-network** buffer sizes:

    $ sudo sysctl net.core.rmem_max=24875  net.core.wmem_max=24875

	net.core.rmem_max = 4235

	net.core.wmem_max = 4235

Set the **per-socket** buffer sizes:

    $ sudo sysctl net.ipv4.tcp_rmem="4096 12437 24875" net.ipv4.tcp_wmem="4096 12437 24875"

    net.ipv4.tcp_rmem = 4096 12437 24875

    net.ipv4.tcp_wmem = 4096 12437 24875

And it's done! Testing this is left as an exercise for the
reader. Note that in my experience this is less useful on wireless
connections.


On Units
========

As previously stated, in this module you will find two very similar
sets of classes available. These are the **NIST** and **SI**
prefixes. The **NIST** prefixes are all base 2 and have an 'i'
character in the middle. The **SI** prefixes are base 10 and have no
'i' character.

For smaller values, these two systems of unit prefixes are roughly
equivalent. The ``round()`` operations below demonstrate how close in
a percent one "unit" of SI is to one "unit" of NIST.

    In [15]: one_kilo = 1 * 10**3

    In [16]: one_kibi = 1 * 2**10

    In [17]: round(one_kilo / float(one_kibi), 2)

    Out[17]: 0.98

    In [18]: one_tera = 1 * 10**12

    In [19]: one_tebi = 1 * 2**40

    In [20]: round(one_tera / float(one_tebi), 2)

    Out[20]: 0.91

    In [21]: one_exa = 1 * 10**18

    In [22]: one_exbi = 1 * 2**60

    In [23]: round(one_exa / float(one_exbi), 2)

    Out[23]: 0.87

They begin as roughly equivalent, however as you can see, they diverge
significantly for higher values.

Why two unit systems? Why take the time to point this difference out?
Why should you care? The Linux Documentation Project comments on
that:

    Before these binary prefixes were introduced, it was fairly common
    to use k=1000 and K=1024, just like b=bit, B=byte.  Unfortunately,
    the M is capital already, and cannot be capitalized to indicate
    binary-ness.

    At first that didn't matter too much, since memory modules and
    disks came in sizes that were powers of two, so everyone knew that
    in such contexts "kilobyte" and "megabyte" meant 1024 and 1048576
    bytes, respectively.  What originally was a sloppy use of the
    prefixes "kilo" and "mega" started to become regarded as the "real
    true meaning" when computers were involved.  But then disk
    technology changed, and disk sizes became arbitrary numbers.
    After a period of uncertainty all disk manufacturers settled on
    the standard, namely k=1000, M=1000k, G=1000M.

    The situation was messy: in the 14k4 modems, k=1000; in the 1.44MB
    diskettes, M=1024000; etc.  In 1998 the IEC approved the standard
    that defines the binary prefixes given above, enabling people to
    be precise and unambiguous.

    Thus, today, MB = 1000000B and MiB = 1048576B.

    In the free software world programs are slowly being changed to
    conform.  When the Linux kernel boots and says

        hda: 120064896 sectors (61473 MB) w/2048KiB Cache

    the MB are megabytes and the KiB are kibibytes.

- Source: ``man 7 units`` - http://man7.org/linux/man-pages/man7/units.7.html

Furthermore, to quote the National Institute of Standards and
Technology (NIST):

    "Once upon a time, computer professionals noticed that 210 was
    very nearly equal to 1000 and started using the SI prefix "kilo"
    to mean 1024. That worked well enough for a decade or two because
    everybody who talked kilobytes knew that the term implied 1024
    bytes. But, almost overnight a much more numerous "everybody"
    bought computers, and the trade computer professionals needed to
    talk to physicists and engineers and even to ordinary people, most
    of whom know that a kilometer is 1000 meters and a kilogram is
    1000 grams.

    "Then data storage for gigabytes, and even terabytes, became
    practical, and the storage devices were not constructed on binary
    trees, which meant that, for many practical purposes, binary
    arithmetic was less convenient than decimal arithmetic. The result
    is that today "everybody" does not "know" what a megabyte is. When
    discussing computer memory, most manufacturers use megabyte to
    mean 220 = 1 048 576 bytes, but the manufacturers of computer
    storage devices usually use the term to mean 1 000 000 bytes. Some
    designers of local area networks have used megabit per second to
    mean 1 048 576 bit/s, but all telecommunications engineers use it
    to mean 106 bit/s. And if two definitions of the megabyte are not
    enough, a third megabyte of 1 024 000 bytes is the megabyte used
    to format the familiar 90 mm (3 1/2 inch), "1.44 MB" diskette. The
    confusion is real, as is the potential for incompatibility in
    standards and in implemented systems.

    "Faced with this reality, the IEEE Standards Board decided that
    IEEE standards will use the conventional, internationally adopted,
    definitions of the SI prefixes. Mega will mean 1 000 000, except
    that the base-two definition may be used (if such usage is
    explicitly pointed out on a case-by-case basis) until such time
    that prefixes for binary multiples are adopted by an appropriate
    standards body."

Source: http://physics.nist.gov/cuu/Units/binary.html
