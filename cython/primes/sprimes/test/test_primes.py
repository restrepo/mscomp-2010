"""Simple correctness tests for primes codes."""

def check_20(primes):
    """Check the first 20 primes against a hardcoded list."""
    PRIMES_20 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71]
    primes_20 = primes(20)
    assert primes_20 == PRIMES_20,"Mismatch in first 20 primes"

def test_pyx():
    """Test Cython version"""
    from sprimes.primes import primes
    check_20(primes)

def test_py():
    """Test pure python version"""
    from sprimes.pyprimes import primes
    check_20(primes)
