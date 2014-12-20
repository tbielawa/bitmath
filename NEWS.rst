NEWS
####

.. contents::
   :depth: 1
   :local:

.. _bitmath-1.1.0-0:

bitmath-1.1.0-1
***************

bitmath-1.1.0-1 was published on 2014-12-20.

* `GitHub Milestone Tracker for 1.1.0 <https://github.com/tbielawa/bitmath/milestones/1.1.0>`_

Changes
=======

**Added Functionality**

* New ``bitmath`` `command-line tool
  <https://github.com/tbielawa/bitmath/issues/35>`_ added. Provides
  CLI access to basic unit conversion functions
* New utility function `bitmath.parse_string
  <http://bitmath.readthedocs.org/en/latest//module.html#bitmath-parse-string>`_
  for parsing a human-readable string into a bitmath object. `Patch
  submitted <https://github.com/tbielawa/bitmath/pull/42>`_ by new
  contributor `tonycpsu <https://github.com/tonycpsu>`_.



.. _bitmath-1.0.8-1:

bitmath-1.0.5-1 through 1.0.8-1
*******************************

bitmath-1.0.8-1 was published on 2014-08-14.

* `GitHub Milestone Tracker for 1.0.8 <https://github.com/tbielawa/bitmath/issues?q=milestone%3A1.0.8>`_

Major Updates
=============

* bitmath has a proper documentation website up now on Read the Docs,
  check it out: `bitmath.readthedocs.org
  <http://bitmath.readthedocs.org/en/latest/>`_
* bitmath is now Python 3.x compatible
* bitmath is now included in the `Extra Packages for Enterprise Linux
  <https://fedoraproject.org/wiki/EPEL>`_ `EPEL6
  <http://dl.fedoraproject.org/pub/epel/6/x86_64/repoview/python-bitmath.html>`_
  and `EPEL7
  <http://dl.fedoraproject.org/pub/epel/7/x86_64/repoview/python-bitmath.html>`_
  repositories
* merged 6 `pull requests
  <https://github.com/tbielawa/bitmath/pulls?q=is%3Apr+closed%3A%3C2014-08-28>`_
  from 3 `contributors
  <https://github.com/tbielawa/bitmath/graphs/contributors>`_

Bug Fixes
=========

* fixed some math implementation bugs

  * `commutative multiplication <https://github.com/tbielawa/bitmath/issues/18>`_
  * `true division <https://github.com/tbielawa/bitmath/issues/2>`_

Changes
=======

**Added Functionality**

* `best-prefix
  <http://bitmath.readthedocs.org/en/latest/instances.html#best-prefix>`_
  guessing: automatic best human-readable unit selection
* support for `bitwise operations
  <http://bitmath.readthedocs.org/en/latest/simple_examples.html#bitwise-operations>`_
* `formatting customization
  <http://bitmath.readthedocs.org/en/latest/instances.html#format>`_
  methods (including plural/singular selection)
* exposed many more `instance attributes
  <http://bitmath.readthedocs.org/en/latest/instances.html#instances-attributes>`_
  (all instance attributes are usable in custom formatting)
* a `context manager
  <http://bitmath.readthedocs.org/en/latest/module.html#bitmath-format>`_
  for applying formatting to an entire block of code
* utility functions for sizing `files
  <http://bitmath.readthedocs.org/en/latest/module.html#bitmath-getsize>`_
  and `directories
  <http://bitmath.readthedocs.org/en/latest/module.html#bitmath-listdir>`_
* add `instance properties
  <http://bitmath.readthedocs.org/en/latest/instances.html#instance-properties>`_
  equivalent to ``instance.to_THING()`` methods

Project
=======

**Tests**

* Test suite is now implemented using `Python virtualenv's
  <https://github.com/tbielawa/bitmath/blob/master/Makefile#L177>`_
  for consistency across across platforms
* Test suite now contains 150 unit tests. This is **110** more tests
  than the previous major release (:ref:`1.0.4-1 <bitmath-1.0.4-1>`)
* Test suite now runs on EPEL6 and EPEL7
* `Code coverage
  <https://coveralls.io/r/tbielawa/bitmath?branch=master>`_ is stable
  around 95-100%


.. _bitmath-1.0.4-1:

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
