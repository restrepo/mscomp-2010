# Simple makefile to drive the update/install of python packages

# Configure this variable according to your local setup
PYPREFIX ?= $(HOME)/usr/local
#PYPREFIX ?= $(HOME)/usr/opt

export PYPREFIX := $(PYPREFIX)

# Version of python and prefix you want to use.  This MUST be of the form
# 'pythonX.Y' (where X.Y means Major.Minor version numbers) since that is the
# form used by Python in constructing paths once --prefix is specified for
# distutils-based installation.
PYTHON ?= python2.6
export PYTHON := $(PYTHON)

# Basic setup, update and install from svn all the main packages.
all: numpy scipy matplotlib
#all: numpy scipy matplotlib ipython
#all: numpy matplotlib scipy ipython nipy

allt: tnumpy matplotlib tscipy

# Individual build targets
ipython: showprefix
	./makepkg ipython

numpy: showprefix
	./makepkg numpy

scipy: showprefix
	./makepkg scipy

# Targets that call the test suite immediately.  The nasty subshell/redirection
# trickery is there to get *both* stdout and stderr (nose prints to stderr) to
# end up *both* on the screen and in a log file.
tnumpy: numpy
	(./testpkg numpy | tee tests_numpy.log ) 3>&1 1>&2 2>&3 | \
	tee -a tests_numpy.log  

tscipy: scipy
	(./testpkg scipy | tee tests_scipy.log ) 3>&1 1>&2 2>&3 | \
	tee -a tests_scipy.log  

# Matplotlib requires a bit of extra manual cleanup
matplotlib: showprefix
	rm -rf $(PYPREFIX)/lib/$(PYTHON)/site-packages/pytz
	rm -rf $(PYPREFIX)/lib/$(PYTHON)/site-packages/dateutil
	rm -rf $(PYPREFIX)/lib/$(PYTHON)/site-packages/pylab*
	./makepkg matplotlib

# Cleaup some junk left over by the scipy test suite (it's a weave bug)
clean:
	rm -f sc_*.cpp sc_*.so linux*compiled_catalog *~

# A target to check out the above from their respective version control
# systems.  Note that you must have bzr and svn installed!
checkout:
	bzr co lp:ipython
	svn co http://svn.scipy.org/svn/numpy/trunk numpy
	svn co http://svn.scipy.org/svn/scipy/trunk scipy
	svn co https://matplotlib.svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib matplotlib

# Common target used by others to show build prefix
showprefix:
	@echo "##############################################################"
	@echo "PYPREFIX set to: $(PYPREFIX)"
	@echo "##############################################################"

