========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |coveralls| |codecov|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/zfit-flavour/badge/?style=flat
    :target: https://readthedocs.org/projects/zfit-flavour
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/zfit/zfit-flavour.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/zfit/zfit-flavour

.. |coveralls| image:: https://coveralls.io/repos/zfit/zfit-flavour/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/zfit/zfit-flavour

.. |codecov| image:: https://codecov.io/github/zfit/zfit-flavour/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/zfit/zfit-flavour

.. |codacy| image:: https://img.shields.io/codacy/grade/[Get ID from https://app.codacy.com/app/zfit/zfit-flavour/settings].svg
    :target: https://www.codacy.com/app/zfit/zfit-flavour
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/zfit-flavour.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/zfit-flavour

.. |wheel| image:: https://img.shields.io/pypi/wheel/zfit-flavour.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/zfit-flavour

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/zfit-flavour.svg
    :alt: Supported versions
    :target: https://pypi.org/project/zfit-flavour

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/zfit-flavour.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/zfit-flavour

.. |commits-since| image:: https://img.shields.io/github/commits-since/zfit/zfit-flavour/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/zfit/zfit-flavour/compare/v0.0.1...master



.. end-badges

Flavour physics for zfit

* Free software: BSD 3-Clause License

Installation
============

::

    pip install zfit-flavour

You can also install the in-development version with::

    pip install https://github.com/zfit/zfit-flavour/archive/master.zip


Documentation
=============


https://zfit-flavour.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
