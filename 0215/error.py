#!/usr/bin/env python
"""
File with deliberate  errors to illustrate interactive debugging
"""

from numpy import *
import time,sys

import sys


def explode():
    a = 'a local variable'
    print 'now, we blow up!'
    1/0

class foo:
    """foo class docstring"""
    def __init__(self):
        """init ds"""
        pass

class bar:
    """bar class docstring"""
    def __init__(self):
        """bar init ds"""
        pass
    def __call__(self):
        """call ds"""
        print 'bar called!'


def Ramp(result, size, start, end):
    step = (end-start)/(size-1)
    for i in xrange(size):
        result[i] = start + step*i

def RampNum(result, size, start, end):
    tmp = zeros(size+1)
    step = (end-start)/(size-1-tmp)
    result[:] = arange(size)*step + start

def main():
    size = 6
    reps = 5
    print 'reps:',reps
    array_normal = [0]*size
    t0=time.clock()
    for i in xrange(reps):
        Ramp(array_normal, size, 0.0, 1.0)
    Rtime = time.clock()-t0
    print 'Ramp time:', Rtime

    t0=time.clock()
    array_num = zeros(size,'d')
    for i in xrange(reps):
        RampNum(array_num, size, 0.0, 1.0)
    RNtime = time.clock()-t0
    print 'RampNum time:', RNtime

    print 'speedup:',Rtime/RNtime


if __name__ == '__main__':
    explode()
    main()
