=============================
 Simple demo of using Cython
=============================

This simple demo uses a naive prime number algorithm to illustrate how Python
code can be converted to Cython for speed, with often minimal effort.  It is a
slightly cleaned up and commented version of the demo included with Cython.

To do the initial build of the module, simply type::

  make

You should note that the included Makefile is configured to do an in-place
build of the extensions.  You should therefore make sure that you symlink the
``sprimes`` directory somewhere in your ``$PYTHONPATH``.

A quick test of the resulting improvements::

  In [1]: from sprimes import primes,pyprimes

  In [3]: %timeit primes.primes(1000)
  100 loops, best of 3: 3 ms per loop

  In [4]: %timeit pyprimes.primes(1000)
  10 loops, best of 3: 119 ms per loop

Note that the code also contains some trivial code and doctests, meant to
illustrate the testing of extension modules and not any particular features of
Cython.


Testing notes
=============

By default, the standard python tools fail to properly recognize doctests in
extension modules.  After installing the IPython doctest plugin,  you should be
able to run the test suite by typing::

  make test

and you should see something similar to::

  maqroll[primes]> make test
  python setup.py build_ext --inplace
  running build_ext
  nosetests -s --with-extdoctest --doctest-tests --exe sprimes
  ............
  ----------------------------------------------------------------------
  Ran 12 tests in 0.021s

  OK

