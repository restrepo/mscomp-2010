"""Simple univariate polynomial example."""

import numpy as np

def prod(seq):
    """Multiply the elements of a sequence."""
    return reduce(lambda x,y: x*y, seq, 1)

a = np.array([3.4, 4.5])
b = np.array([2.1, 5.5])
k = 0.5

x2 = np.poly1d([1, 0, 0])
den_roots = -b/a
den = np.poly1d(den_roots, r=True)

denoms = [ np.poly1d([1, -di]) for di in den_roots ]

num_terms  = [ (prod([dj for (j, dj) in enumerate(denoms) if j != i ]))
               for i in range(len(a)) ]

num = sum(num_terms)

R = x2*num - k*den
R /= R.coeffs[0]

print 'R(x) = \n', R
print 'Roots:', R.r
