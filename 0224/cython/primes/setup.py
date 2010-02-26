#!/usr/bin/env python

import glob

from distutils.core import setup
from distutils.extension import Extension

from Cython.Distutils import build_ext

# Main script
ext_modules=[ Extension("sprimes.primes", ["sprimes/primes.pyx"]),
              ]

setup(
  name        = 'Simple Primes Cython Demo',
  cmdclass    = {'build_ext': build_ext},
  packages    = ['sprimes','sprimes.test'],
  ext_modules = ext_modules,
)
