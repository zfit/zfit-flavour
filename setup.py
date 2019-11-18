#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
import os
import glob
from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as requirements_file:
    requirements = requirements_file.read().splitlines()

with open(os.path.join(here, 'requirements_dev.txt'), encoding='utf-8') as requirements_dev_file:
    requirements_dev = requirements_dev_file.read().splitlines()

# split the developer requirements into setup and test requirements
if not requirements_dev.count("") == 1 or requirements_dev.index("") == 0:
    raise SyntaxError("requirements_dev.txt has the wrong format: setup and test "
                      "requirements have to be separated by one blank line.")
requirements_dev_split = requirements_dev.index("")

setup_requirements = ["pip>9",
                      "setuptools_scm",
                      "setuptools_scm_git_archive"]
test_requirements = requirements_dev[requirements_dev_split + 1:]  # +1: skip empty line

setup(
    name='zfit-flavour',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/zfit_flavour/_version.py',
        'fallback_version': '0.0.1',
    },
    license='BSD-3-Clause',
    description='Flavour physics for zfit',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Jonas Eschle, Rafael Silva Coutinho',
    author_email='Jonas.Eschle@cern.ch, rafael.silva.coutinho@cern.ch',
    url='https://github.com/zfit/zfit-flavour',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('zfit_flavour/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://zfit-flavour.readthedocs.io/',
        'Changelog': 'https://zfit-flavour.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/zfit/zfit-flavour/issues',
    },
    keywords=[
        'flavour', 'zfit', 'model fitting'
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,

)
