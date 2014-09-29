NEWS
####

.. contents::
   :depth: 1
   :local:


bitmath-1.0.5-1 through 1.0.8-1
*******************************

bitmath-1.0.8-1 was published on 2014-08-14.

Major Updates
=============

* bitmath has a proper documentation website up now on Read the Docs,
  check it out:
* [bitmath.readthedocs.org] [1]
* bitmath is now Python 3.x compatible
* bitmath is now included in the [Extra Packages for Enterprise Linux] [2] [EPEL6] [3] and [EPEL7] [4] repositories
* merged 6 [pull requests] [12] from 3 [contributors] [13]

Bug Fixes
=========

* fixed some math implementation bugs
  * [commutative multiplication] [14]
  * [true division] [15]

Changes
=======

**Added Functionality**

* [best-prefix] [5] guessing: automatic best human-readable unit
  selection
* support for [bitwise operations] [6]
* [formatting customization] [7] methods (including plural/singular
  selection)
* exposed many more [instance attributes] [11] (all instance
  attributes are usable in custom formatting)
* a [context manager] [8] for applying formatting to an entire block
  of code
* utility functions for sizing [files] [9] and [directories] [10]
* add [instance properties] [16] equivalent to instance.to_THING()
  methods

Project
=======

**Tests**

* Test suite is now implemented using [Python virtualenv's] [17] for
  consistency across across platforms
* Test suite now contains 150 unit tests. This is **110** more tests
  than the previous major release (1.0.4-1)
* Test suite now runs on EPEL6 and EPEL7
* [Code coverage] [18] is stable around 95-100%



  [1]: http://bitmath.readthedocs.org/en/latest/ "bitmath.readthedocs.org"
  [2]: https://fedoraproject.org/wiki/EPEL "Extra Packages for Enterprise Linux"
  [3]: http://dl.fedoraproject.org/pub/epel/6/x86_64/repoview/python-bitmath.html "EPEL6"
  [4]: http://dl.fedoraproject.org/pub/epel/7/x86_64/repoview/python-bitmath.html "EPEL7"
  [5]: http://bitmath.readthedocs.org/en/latest/instances.html#best-prefix "Documentation for best-prefix guessing"
  [6]: http://bitmath.readthedocs.org/en/latest/simple_examples.html#bitwise-operations "Table of supported bitwise operations"
  [7]: http://bitmath.readthedocs.org/en/latest/instances.html#format "Documentation for custom formatting"
  [8]: http://bitmath.readthedocs.org/en/latest/module.html#bitmath-format "Documentation for the formatting context manager"
  [9]: http://bitmath.readthedocs.org/en/latest/module.html#bitmath-getsize "Documentation for the getsize function"
  [10]: http://bitmath.readthedocs.org/en/latest/module.html#bitmath-listdir "Documentation for the listdir function"
  [11]: http://bitmath.readthedocs.org/en/latest/instances.html#instances-attributes "Documentation for instance attributes"
  [12]: https://github.com/tbielawa/bitmath/pulls?q=is%3Apr+closed%3A%3C2014-08-28 "Pull requests from 1.0.4-1 through 1.0.8-3"
  [13]: https://github.com/tbielawa/bitmath/graphs/contributors "Project Contributors"
  [14]: https://github.com/tbielawa/bitmath/issues/18 "GitHub issue for multiplication bug"
  [15]: https://github.com/tbielawa/bitmath/issues/2 "GitHub issue for division bug"
  [16]: http://bitmath.readthedocs.org/en/latest/instances.html#instance-properties "Documentation for instance properties"
  [17]: https://github.com/tbielawa/bitmath/blob/master/Makefile#L177 "Test suite entry point for virtualenv tests"
  [18]: https://coveralls.io/r/tbielawa/bitmath?branch=master "Code coverage report"


bitmath-1.0.4-1
***************

This is the first release of **bitmath**. bitmath-1.0.4-1 was
published on 2014-03-20.

Project
=======

Available via:

* `PyPi <https://pypi.python.org/pypi/bitmath/>`_
* `Fedora 19 <https://admin.fedoraproject.org/updates/FEDORA-2014-4235/python-bitmath-1.0.4-1.fc19>`_
* `Fedora 20 <https://admin.fedoraproject.org/updates/FEDORA-2014-4235/python-bitmath-1.0.4-1.fc20>`_

bitmath had been under development for 12 days when the 1.0.4-1
release was made available.

Debut Functionality
===================

* Converting between **SI** and **NIST** prefix units (``GiB`` to ``kB``)
* Converting between units of the same type (SI to SI, or NIST to NIST)
* Basic arithmetic operations (subtracting 42KiB from 50GiB)
* Rich comparison operations (``1024 Bytes == 1KiB``)
* Sorting
* Useful *console* and *print* representations
