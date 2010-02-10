"""Simple multiplot example with Bessel functions and their zeros.
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy import special


def fplot(func, xgrid=(0, 10, 200), ax=None):
    x = np.linspace(*xgrid)
    y = func(x)
    if ax is None:
        ax = plt.gca()
    ax.plot(x, y)
    return ax


if __name__ == '__main__':
    import sys
    print 'ARGV:', sys.argv
    fig = plt.figure()
    zcolors = ['red', 'green']
    s = special
    xmax = 10
    to_plot = [(s.jn, s.jn_zeros, 'Bessel 1st kind (J)'),
               (s.yn, s.yn_zeros, 'Bessel 2nd kind (Y)')]
    for i, (func, func_zeros, title) in enumerate(to_plot):
        ax = fig.add_subplot(2, 1, i+1)
        ax.axhline(0, color='black')
        for n in (0,1):
            fplot(lambda x: func(n, x), ax=ax)
            z = func_zeros(n, 8)
            z = z[z<=xmax]
            ax.scatter(z, np.zeros_like(z), color=zcolors[n])
            ax.set_title(title)
    
    plt.show()
