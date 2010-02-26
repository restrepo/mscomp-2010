#!/usr/bin/env python
"""Simple demo of Fibonacci numbers construction  in Fortran."""

from __future__ import print_function

import numpy as np

from example import fib

npts = 17
a = np.empty(npts)
fib(a)

print('The first', npts, 'Fibonacci numbers:\n', a)
