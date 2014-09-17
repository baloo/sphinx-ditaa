# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains a ditaa_ Sphinx_ extension.

.. _ditaa: http://ditaa.sourceforge.net/
.. _Sphinx: http://sphinx.pocoo.org/

ditaa_ is a program and a reStructuredText_ directive to allow embeded ASCII
art figures to be rendered as nice images. The
ditaa_ directive needs a *hardcoded* image format, so it doesn't goes well
with Sphinx_ multi-format support.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

This extension adds the ``ditaa`` directive that automatically directive that automatically selects the
image format to use acording to the Sphinx_ writer used to generate the
documentation.

Usage example::

    .. ditaa::

      +--------+   +-------+    +-------+
      |        | --+ ditaa +--> |       |
      |  Text  |   +-------+    |diagram|
      |Document|   |!magic!|    |       |
      |     {d}|   |       |    |       |
      +---+----+   +-------+    +-------+
          :                         ^
          |       Lots of work      |
          +-------------------------+
'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-ditaa',
    version='0.1',
    url='http://packages.python.org/sphinxcontrib-ditaa/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-ditaa',
    license='BSD License',
    author='Arthur Gautier',
    description='ditaa Sphinx extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
