#!/usr/bin/env python
from setuptools import setup

setup(name='sphinx-ditaa',
      description="""
        A basic ditaa builder for sphinx""",
      version='0.1',
      install_requires=['sphinx>=1.0'],
      packages=['sphinx/ext'],
      # namespace_packages=['sphinx.ext'],
      author='Arthur Gautier',
      url='https://github.com/baloo/sphinx-ditaa',
      )
