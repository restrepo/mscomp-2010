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
