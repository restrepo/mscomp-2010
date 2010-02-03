"""Illustrating error propagation by iterating the logistic map.

Inspired by :http://us.pycon.org/2009/conference/schedule/event/65/

Study different forms of writing:

f(x) = r*x*(1-x)

Write the above function in three algebraically equivalent forms, and study
their behavior under iteration.  See for what values of r all forms evolve
identically and for which ones they don't.
"""

import matplotlib.pyplot as plt

# Interesting values to try for r:
# [1.9, 2.9, 3.1, 3.5, 3.9]
r = 3.5 # global default
x0 = 0.6  # any number in [0,1] will do here
numpoints = 100
