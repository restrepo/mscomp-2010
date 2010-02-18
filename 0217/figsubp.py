"""Implement fig_subplot for matplotlib."""

import matplotlib.pyplot as plt


def share_axes(fig, nrows, ncols, to_share, idx, **subplot_kw):
    """Turn on axis sharing for the given list of figure and axes"""
    # Must make axes as dict so we can point all others to shared one
    axd = {}
    axd[idx] = fig.add_subplot(nrows, ncols, idx, **subplot_kw)
    # Valid indices for axes start at 1, since fig is at 0: 
    indices = set(range(1, nrows*ncols+1))
    indices.remove(idx)
    subplot_kw[to_share] = axd[idx]
    for i in indices:
        axd[i] = fig.add_subplot(nrows, ncols, i, **subplot_kw)
    # Now, we need axes to be an ordered list:
    axes = [axd[i] for i in sorted(axd.keys())]

    return axes


def fig_subplot(subplots=(1,1), sharex=None, sharey=None, subplot_kw=None,
                **fig_kw):
    """Create a figure with a set of subplots already made.

    This utility wrapper makes it convenient to create common layouts of
    subplots, including the enclosing figure object, in a single call.

    Parameters
    ----------
    subplots : 2-tuple, optional
      Number of rows and columns of the subplot grid.  Defaults to (1,1).

    sharex : int, optional
      The index of which axis to share the X axis for. Note that axes are
      created with a counter starting from 1.

    sharey : int, optional
      Like sharex, but for sharing the Y axis.  Note that currently, sharing
      *both* X and Y axes is not supported via this routine.
      
    subplot_kw : dict, optional
      Dict with keywords passed to the add_subplot() call used to create each
      subplots.

    fig_kw : dict, optional
      Dict with keywords passed to the figure() call.

    Returns
    -------
    fig_axes : list    
      A list containing [fig, ax1, ax2, ...], where fig is the Matplotlib
      Figure object and the rest are the axes.

    Examples
    --------
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x**2)

    plt.close('all')

    # Just a figure and one subplot
    f, ax = fig_subplot((1,1))
    ax.plot(x, y)
    ax.set_title('Simple plot')
    
    # Two subplots, grab the whole fig_axes list
    fax = fig_subplot((2,1), sharex=1)
    fax[1].plot(x, y)
    fax[1].set_title('Shared X axes')
    fax[2].scatter(x, y)

    # Two subplots, unpack the output immediately
    f, ax1, ax2 = fig_subplot((1,2), sharey=1)
    ax1.plot(x, y)
    ax1.set_title('Shared Y axes')
    ax2.scatter(x, y)
    """

    # XXX I think this is doable, I just ran out of time now to implement it
    if sharex and sharey:
        raise NotImplementedError('both axes shared not implemented')
    
    if subplot_kw is None:
        subplot_kw = {}
        
    fig = plt.figure(**fig_kw)
    nrows, ncols = subplots
    ax_idx = range(1, nrows*ncols+1)

    if sharex:
        axes = share_axes(fig, nrows, ncols, 'sharex', sharex, **subplot_kw)
    elif sharey:
        axes = share_axes(fig, nrows, ncols, 'sharey', sharey, **subplot_kw)
        #raise NotImplementedError('sharey not ready yet')
    else:
        axes = [ fig.add_subplot(nrows, ncols, i, **subplot_kw)
                 for i in ax_idx ]
    return [fig] + axes


if __name__ == '__main__':
    # Simple demo
    import numpy as np
    
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x**2)

    plt.close('all')

    # Just a figure and one subplot
    f, ax = fig_subplot((1,1))
    ax.plot(x, y)
    ax.set_title('Simple plot')
    
    # Two subplots, grab the whole fig_axes list
    fax = fig_subplot((2,1), sharex=1)
    fax[1].plot(x, y)
    fax[1].set_title('Shared X axes')
    fax[2].scatter(x, y)

    # Two subplots, unpack the output immediately
    f, ax1, ax2 = fig_subplot((1,2), sharey=1)
    ax1.plot(x, y)
    ax1.set_title('Shared Y axes')
    ax2.scatter(x, y)

    plt.show()
