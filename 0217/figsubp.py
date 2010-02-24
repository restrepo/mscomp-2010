"""Implement fig_subplot for matplotlib."""

import matplotlib.pyplot as plt

def fig_subplot(nrows=1, ncols=1, sharex=False, sharey=False,
                subplot_kw=None, **fig_kw):
    """Create a figure with a set of subplots already made.

    This utility wrapper makes it convenient to create common layouts of
    subplots, including the enclosing figure object, in a single call.

    Parameters
    ----------
    nrows : int, optional
      Number of rows of the subplot grid.  Defaults to 1.

    nrows : int, optional
      Number of columns of the subplot grid.  Defaults to 1.

    sharex : bool, optional
      If True, the X axis will be shared amongst all subplots.

    sharex : bool, optional
      If True, the Y axis will be shared amongst all subplots.

    subplot_kw : dict, optional
      Dict with keywords passed to the add_subplot() call used to create each
      subplots.

    fig_kw : dict, optional
      Dict with keywords passed to the figure() call.  Note that all keywords
      not recognized above will be automatically included here.

    Returns
    -------
    fig_axes : list    
      A list containing [fig, ax1, ax2, ...], where fig is the Matplotlib
      Figure object and the rest are the axes.

    Examples
    --------
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    # Just a figure and one subplot
    f, ax = fig_subplot()
    ax.plot(x, y)
    ax.set_title('Simple plot')
    
    # Two subplots, unpack the output immediately
    f, ax1, ax2 = fig_subplot(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')
    ax2.scatter(x, y)

    # Four polar axes
    fig_subplot(2, 2, subplot_kw=dict(polar=True))
    """

    if subplot_kw is None:
        subplot_kw = {}
        
    fig = plt.figure(**fig_kw)

    # Create first subplot separately, so we can share it if requested
    ax1 = fig.add_subplot(nrows, ncols, 1, **subplot_kw)
    if sharex:
        subplot_kw['sharex'] = ax1
    if sharey:
        subplot_kw['sharey'] = ax1

    # Valid indices for axes start at 1, since fig is at 0: 
    axes = [ fig.add_subplot(nrows, ncols, i, **subplot_kw)
             for i in range(2, nrows*ncols+1)]

    return [fig, ax1] + axes


if __name__ == '__main__':
    # Simple demo
    import numpy as np
    
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    plt.close('all')

    # Just a figure and one subplot
    f, ax = fig_subplot()
    ax.plot(x, y)
    ax.set_title('Simple plot')
    
    # Two subplots, grab the whole fig_axes list
    fax = fig_subplot(2, sharex=True)
    fax[1].plot(x, y)
    fax[1].set_title('Sharing X axis')
    fax[2].scatter(x, y)

    # Two subplots, unpack the output immediately
    f, ax1, ax2 = fig_subplot(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')
    ax2.scatter(x, y)

    # Three subplots sharing both x/y axes
    f, ax1, ax2, ax3 = fig_subplot(3, sharex=True, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing both axes')
    ax2.scatter(x, y)
    ax3.scatter(x, 2*y**2-1,color='r')
    # Fine-tune figure; make subplots close to each other and hide x ticks for
    # all but bottom plot.
    f.subplots_adjust(hspace=0)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

    # Four polar axes
    fig_subplot(2, 2, subplot_kw=dict(polar=True))

    plt.show()
