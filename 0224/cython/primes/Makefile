# This extension is configured for an in-place build
primes: setup.py sprimes/primes.pyx
	python setup.py build_ext --inplace

test:	primes
	nosetests -s --with-ipdoctest --doctest-tests --exe sprimes

# Run tests without ipython docstring recognition
extest:	primes
	nosetests -s --with-extdoctest --doctest-tests --exe sprimes

clean:
	@echo Cleaning Demos
	@./setup.py clean
	rm -f *.c *.o *.so *~ core *.pyc
	cd sprimes && rm -f *.c *.o *.so *~ core *.pyc
	cd sprimes/test && rm -f *.c *.o *.so *~ core *.pyc
	rm -rf build
