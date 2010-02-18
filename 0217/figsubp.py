"""Implement fig_subplot for matplotlib."""

import matplotlib.pyplot as plt

def share_axes(fig_axes, to_share, idx):
    """Turn on axis sharing for the given list of figure and axes"""
    sharedct = {to_share : idx}
    
    ax_sharex = fig_axes[idx]
    # Valid indices for axes start at 1, since fig is at 0: 
    indices = set( range(1, len(fig_axes) -1))
    indices.remove(idx)
    # We need to disable ticks for all 
    off_ticks = []
    for i in indices:
        ax = fig.add_subplot(nrows, ncols, i, sharex=ax_sharex)
        off_ticks.append(ax.get_xticklabels())
    plt.setp(off_ticks, visible=False)


def fig_subplot(subplots=(1,1), sharex=None, sharey=None, subplot_kw=None,
                **fig_kw):
    """Create a figure with a set of subplots already made.

    This utility wrapper makes it convenient to create common layouts of
    subplots, including the enclosing figure object, in a single call.

    Parameters
    ----------
    subplots : 2-tuple, optional
      Number of rows and columns of the subplot grid.  Defaults to (1,1).

    subplot_kw : dict, optional
      Dict with keywords passed to the add_subplot() call used to create each
      subplots.

    fig_kw : dict, optional
      Dict with keywords passed to the figure() call.

    Returns
    -------
    fig : object
      Matplotlib Figure object.
      
    axes : list
      List of axes
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
        # Must make axes as dict so we can point all others to shared one
        axd = {}
        axd[sharex] = fig.add_subplot(nrows, ncols, sharex, **subplot_kw)
        indices = set(ax_idx)
        indices.remove(sharex)
        sh_ax = axd[sharex]
        for i in indices:
            axd[i] = fig.add_subplot(nrows, ncols, i, sharex=sh_ax,
                                     **subplot_kw)
        # Now, we need axes to be an ordered list:
        axes = [axd[i] for i in sorted(axd.keys())]
    elif sharey:
        raise NotImplementedError('sharey not ready yet')
    else:
        axes = [ fig.add_subplot(nrows, ncols, i, **subplot_kw)
                 for i in ax_idx ]
    return [fig] + axes


# Example
if __name__ == '__main__':
    import numpy as np
    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x**2)

    plt.close('all')
    fax1 = fig_subplot((1,1))
    fax1[1].plot(x, y)

    
    fax2 = fig_subplot((2,1), sharex=1)
    fax2[1].plot(x, y)
    fax2[2].scatter(x, y)

    plt.show()
