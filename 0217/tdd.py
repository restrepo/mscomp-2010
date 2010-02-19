"""Simple example for illustrating test-driven development."""

def f(x):
    """Square x

    >>> f(3)
    9
    """
    return x**2


# tests
import nose, nose.tools as nt

def test_f():
    nt.assert_equals(f(4), 16)


def test_failing():
    x = 5
    x2 = 25
    nt.assert_equals(f(x), x2)


if __name__ == '__main__':
    # This call form is ipython-friendly
    nose.runmodule(argv=['-s','--with-doctest'], exit=False)
