.. image:: https://api.travis-ci.org/tbielawa/bitmath.png
   :target: https://travis-ci.org/tbielawa/bitmath/
   :align: right

.. image:: https://coveralls.io/repos/tbielawa/bitmath/badge.png?branch=master
   :target: https://coveralls.io/r/tbielawa/bitmath?branch=master
   :align: right


bitmath
#######


*bitmath* simplifies many facets of interacting with file sizes in
various units. Functionality includes:

* Converting between **SI** and **NIST** prefix units (``GiB`` to ``kB``)
* Converting between units of the same type (SI to SI, or NIST to NIST)
* Basic arithmetic operations (subtracting 42KiB from 50GiB)
* Rich comparison operations (``1024 Bytes == 1KiB``)
* bitwise operations (``<<``, ``>>``, ``&``, ``|``, ``^``)
* Sorting
* Automatic human-readable prefix selection (like in `hurry.filesize <https://pypi.python.org/pypi/hurry.filesize>`_)

In addition to the conversion and math operations, `bitmath` provides
human readable representations of values which are suitable for use in
interactive shells as well as larger scripts and applications. The
format produced for these representations is customizable via the
functionality included in stdlibs `string.format
<https://docs.python.org/2/library/string.html>`_.

In discussion we will refer to the NIST units primarily. I.e., instead
of "megabyte" we will refer to "mibibyte". The former is ``10^3 =
1,000,000`` bytes, whereas the second is ``2^20 = 1,048,576``
bytes. When you see file sizes or transfer rates in your web browser,
most of the time what you're really seeing are the base-2 sizes/rates.


**Don't Forget!** The source for bitmath `is available on GitHub <https://github.com/tbielawa/bitmath>`_.

Contents
########

.. toctree::
   :maxdepth: 2
   :numbered:

   classes.rst
   instances.rst
   simple_examples.rst
   real_life_examples.rst
   appendices.rst
   copyright.rst







..
   .. automodule:: bitmath
      :members:


..
   Indices and tables
   ==================

      * :ref:`genindex`
      * :ref:`modindex`
      * :ref:`search`
