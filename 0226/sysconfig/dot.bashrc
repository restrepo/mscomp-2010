# .bashrc - started by interactive non-login shells

# useful:
# http://tldp.org/LDP/abs/html/sample-bashrc.html

# Contact: Fernando Perez <fperez@fperez.org>

############################################################################
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

############################################################################
#
# Load basic bash utilities (handy functions and constants)
#
. $HOME/.bash_utils

# Only load system bash_completion if it hasn't been read yet (it defines some
# read-only variables and will error out if you read it twice).
if [[ -z $BASH_COMPLETION && -e /etc/bash_completion ]]; then
    source /etc/bash_completion
fi


############################################################################
#
# Initialize $PATH with sbin locations so I can find system tools
#
export PATH=/usr/local/sbin:/usr/sbin:/sbin:$PATH
#
# Configure paths, using the path generation functions in .bash_utils
#
# These are the prefixes I typically use as --prefix options for installation
# of packages.  There's a method to the madness of having several of them, and
# in this order.  The ones at the top end up first in the generated path specs,
# so they take precedence.
pfx="$pfx $HOME/tmp/junk"  # quick and dirty testing
pfx="$pfx $HOME/tmp/local"  # temporary, stable testing
pfx="$pfx $HOME/usr"  # codes *I* have written
pfx="$pfx $HOME/usr/local"  # default prefix for third-party installs
pfx="$pfx /local"  # used in some machines I work on
pfx="$pfx /opt"  # vendor directory for commercial stuff

# Now, set all common paths based on the prefix list just built.  The
# export_paths function ensures that all commonly needed paths get correctly
# set and exported to the environment.
export_paths "$pfx"

# Default prefix for personal installs I use.
export PREFIX=$HOME/usr/local

# This is the name CMAKE uses for the same thing
export CMAKE_INSTALL_PREFIX=$PREFIX


# Search paths for LaTeX (Dont' forget the final colons.  The null entry `::'
# denotes `default system directories' -- try finding that in the
# documentation.)  Note that these *must* go under ~/texmf, because that
# particular path is hardcoded in LaTeX and is not overridable by the user.
# While one could keep ~/texmf for default package installs and use other
# locations for {tex/bib/bst}inputs, I prefer to centralize all Tex stuff in
# one place.  Since I can't do it in ~/usr/tex, then I'll just keep everything
# TeX related in ~/texmf
export TEXINPUTS=.:$HOME/texmf/texinputs::
export BIBINPUTS=.:$HOME/texmf/bibinputs::
export BSTINPUTS=.:$HOME/texmf/bstinputs::


