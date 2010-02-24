#!/usr/bin/env python
import nose
import pyximport

pyximport.install()
argv = ['nosetests', 'sprimes', '-vvs', '--with-doctest']
nose.main(argv=argv, exit=False)
