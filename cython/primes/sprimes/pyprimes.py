"""Python implementation of primes, plus some trivial tests.

These are code examples tested automatically (trivial in this case):

>>> 1+1
2

>>> 1+2
3
"""

def primes(kmax):
    """Return a list with the first kmax primes.

    Examples:

    >>> primes(1)
    [2]

    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    
    p = []
    k = 0
    n = 2
    while k < kmax:
        i = 0
        while i < k and n % p[i] != 0:
            i += 1
        if i == k:
            p.append(n)
            k += 1
        n += 1
    return p


class Simpleton(object):
    """This is a trivial class.

    It was added here simply to properly exercise doctest, so we can be sure
    that our nose plugin finds doctests embedded in classes and methods as well
    as in top-level functions.

    Example:

    >>> 1+1
    2
    """
    
    def __str__(self):
        """Return string form of instance

        Examples:
        
        >>> s = Simpleton()
        >>> print s
        A simpleton
        """
        
        return "A simpleton"

    def incr(self,x):
        """Increment x by one.

        Examples:
        
        >>> s = Simpleton()
        >>> s.incr(1)
        2
        >>> s.incr(10)
        11
        """
        return x+1

    def decr(self,x):
        """Decrement x by one.

        Examples:
        
        In [8]: s = Simpleton()

        In [9]: s.decr(1)
        Out[9]: 0

        In [10]: s.decr(10)
        Out[10]: 9
        """
        return x-1
