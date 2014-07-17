.. highlight:: python


Real Life Examples
##################

Download Speeds
***************

Let's pretend that your Internet service provider (ISP) advertises
your maximum downstream as **50Mbps** (50 Mega\ **bits** per second)¹
and you want to know how fast that is in Mega\ **bytes** per second?
``bitmath`` can do that for you easily. You can calculate this as
such:

.. code-block:: python
   :linenos:

   >>> from bitmath import *

   >>> downstream = Mib(50)

   >>> print downstream.to_MB()

   MB(6.25)

This tells us that if our ISP advertises **50Mbps** we can expect to
see download rates of nearly **6MiB/sec**.

¹ - *Assuming your ISP follows the common industry practice of using SI (base-10) units to describe file sizes/rates*


Calculating how many files fit on a device
******************************************

Given that we have a thumb drive with 12GiB free, how many 4MiB audio
files can we fit on it?


.. code-block:: python
   :linenos:

   from bitmath import *

   thumb_drive = GiB(12)

   audio_file = MiB(4)

   thumb_drive / audio_file

   3072.0

This tells us that we could fit 3072 4MiB audio files on a 12GiB thumb drive.


Printing Human-Readable File Sizes in Python
********************************************

In a Python script or intrepreter we may wish to print out file sizes
in something other than bytes (which is what ``os.path.getsize``
returns). We can use ``bitmath`` to do that too:


.. code-block:: python
   :linenos:

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



Calculating Linux BDP and TCP Window Scaling
********************************************

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

#. Measure the latency, or round trip time (RTT), between the host we're tuning and our target remote host
#. Measure/identify our network transfer rate
#. Calculate the BDP (multiply transfer rate by rtt)
#. Obtain our current kernel settings
#. Adjust settings as necessary

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

Remember 1 Byte = 8 Bits:

.. code-block:: python

   tx_rate_GB = 1/8 = 0.125

Our equivalent transfer rate is 0.125GB/sec.

- Convert our RTT from miliseconds into seconds

Remember 1ms = 10^-3s:

.. code-block:: python

   window_seconds = 0.199 * 10^-3 = 0.000199

Our equivalent RTT window is 0.000199s

- Next we multiply the transfer rate by the length of our RTT window (in seconds)

(The unit analysis for this is ``GB/s * s`` leaving us with ``GB``)

.. code-block:: python

   BDP = rx_rate_GB * window_seconds = 0.125 * 0.000199 = 0.000024875

Our BDP is 0.000024875GB.

- Convert 0.000024875GB to bytes:

Remember 1GB = 10^9B

.. code-block:: python

   BDP_bytes = 0.000024875 * 10^9 = 24875.0

Our BDP is 24875 bytes (or about 24.3KiB)

**Calculate with bitmath**

All of this math can be done much quicker (and with greater accuracy)
using the bitmath library. Let's see how:

.. code-block:: python
   :linenos:

   from bitmath import GB

   tx = 1/8.0

   rtt = 0.199 * 10**-3

   bdp = (GB(tx * rtt)).to_Byte()

   Byte(24875.0)

   bdp.to_KiB()

   KiB(24.2919921875)

**Note:** To avoid integer rounding during division, don't forget to divide by ``8.0`` rather than ``8``

We could shorten that even further:

.. code-block:: python

   print (GB((1/8.0) * (0.199 * 10**-3))).to_Byte()

   24875.0Byte

**Get the current kernel parameters**

Important to note is that the **per-socket** buffer sizes must not
exceed the **core network** buffer sizes. Lets fetch our current core
buffer sizes:

.. code-block:: console

   $ sysctl net.core.rmem_max net.core.wmem_max
   net.core.rmem_max = 212992
   net.core.wmem_max = 212992

Recall, these values are in bytes. What are they in KiB?

.. code-block:: python

   >>> Byte(212992).to_KiB()

   KiB(208.0)

This means our core networking buffer sizes are set to 208KiB
each. Now let's check our current per-socket buffer sizes:

.. code-block:: console

   $ sysctl net.ipv4.tcp_rmem net.ipv4.tcp_wmem
   net.ipv4.tcp_rmem = 4096        87380   6291456
   net.ipv4.tcp_wmem = 4096        16384   4194304

Let's double-check that our buffer sizes aren't already out of wack
(per-socket should be <= networking core)

.. code-block:: python

   >>> net_core_max = KiB(bytes=212992)

   >>> ipv4_tcp_rmem_max = KiB(bytes=6291456)

   >>> ipv4_tcp_rmem_max > net_core_max

   True

It appears that my buffers aren't sized appropriately. We'll fix that
when we set the tunable parameters.

Finally, how large is the entire system TCP buffer?

.. code-block:: console

   $ sysctl net.ipv4.tcp_mem
   net.ipv4.tcp_mem = 280632       374176  561264

Our max system TCP buffer size is set to **561264**. Recall that this
parameter is measured in **memory pages**. Most of the time your page
size is ``4096 bytes``, but you can check by running the command:
``getconf PAGESIZE``. To convert the system TCP buffer size
(561264) into a byte-based unit, we'll multiply it by our pagesize
(4096):

.. code-block:: python

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

.. code-block:: console

   $ sudo sysctl net.core.rmem_max=24875  net.core.wmem_max=24875
   net.core.rmem_max = 4235
   net.core.wmem_max = 4235

Set the **per-socket** buffer sizes:

.. code-block:: console

   $ sudo sysctl net.ipv4.tcp_rmem="4096 12437 24875" net.ipv4.tcp_wmem="4096 12437 24875"
   net.ipv4.tcp_rmem = 4096 12437 24875
   net.ipv4.tcp_wmem = 4096 12437 24875

And it's done! Testing this is left as an exercise for the
reader. Note that in my experience this is less useful on wireless
connections.
