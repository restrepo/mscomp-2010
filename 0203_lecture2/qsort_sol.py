#!/usr/bin/env python
# coding: utf-8
"""
From Wikipedia:

function quicksort(array)
    var list less, greater
    if length(array) ≤ 1  
        return array  
    select and remove a pivot value pivot from array
    for each x in array
        if x ≤ pivot then append x to less
        else append x to greater
    return concatenate(quicksort(less), pivot, quicksort(greater))

Make this a valid Python program and test it.
"""

def quicksort(array):
    less = []
    greater = []
    
    if len(array) <= 1:
        return array
    #select and remove a pivot value pivot from array
    pivot_idx = 1
    pivot = array.pop(pivot_idx)
    
    for  x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) +  [pivot] + quicksort(greater)

from matplotlib import pyplot as plt

def measure(n1, n2):
    times = []
    sizes = range(n1, n2):
    for n in sizes:
        # a = random(n)
        # measure time for quicksort(a)
        times.append(time)

    plt.plot(sizes, times)
    plt.show()


#if __name__ == '__main__':
