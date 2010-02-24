=============================
 Simple demo of using Cython
=============================

This simple demo uses a naive prime number algorithm to illustrate how Python
code can be converted to Cython for speed, with often minimal effort.  It is a
slightly cleaned up and commented version of the demo included with Cython.


Testing without building
========================

You can test the module by simply running::

    > ./test.py
    Doctest: sprimes.pyprimes ... ok
    Doctest: sprimes.pyprimes.Simpleton ... ok
    Doctest: sprimes.pyprimes.Simpleton.__str__ ... ok
    Doctest: sprimes.pyprimes.Simpleton.incr ... ok
    Doctest: sprimes.pyprimes.primes ... ok
    Test Cython version ... ok
    Test pure python version ... ok

    ----------------------------------------------------------------------
    Ran 7 tests in 0.011s

    OK

This uses Cython's ``pyximport`` feature.  By using::

  In [1]: import pyximport; pyximport.install()

you can import Cython-based modules without configuring/installing them
system-wide.


Building
========

If you want to do a full build of the module, simply type::

  make

You should note that the included Makefile is configured to do an in-place
build of the extensions.  You should therefore make sure that you symlink the
``sprimes`` directory somewhere in your ``$PYTHONPATH``.


Running it
==========

Whether installing it in full or via ``pyximport``, you can now see a quick
test of the resulting improvements::

  In [1]: from sprimes import primes,pyprimes

  In [3]: %timeit primes.primes(1000)
  100 loops, best of 3: 3 ms per loop

  In [4]: %timeit pyprimes.primes(1000)
  10 loops, best of 3: 119 ms per loop

Note that the code also contains some trivial code and doctests, meant to
illustrate the testing of extension modules and not any particular features of
Cython.

.. note::

   By default, the standard python tools fail to properly recognize doctests in
   extension modules.  This can be remedied with a nose plugin such as the
   IPython ipdoctest one, but this is beyond the scope of this simple example.
   