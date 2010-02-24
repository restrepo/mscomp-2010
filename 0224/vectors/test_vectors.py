"""Tests for simple vector implementation."""

# Tests
import nose.tools as nt

from vectors import Vector

def test_creation():
    x = Vector(1, 2)


def test_equality():
    x = Vector(1, 2)
    y = Vector(1, 2)
    nt.assert_equals(x, y)


def test_equality2():
    x = Vector(1, 2)
    y = Vector(1, 3)
    nt.assert_not_equals(x, y)


def test_equality3():
    x = Vector(1, 2)
    y = Vector([1, 2])
    nt.assert_equals(x, y)


def test_addition():
    x = Vector(1, 2)
    y = Vector(1, 3)
    z = Vector(2, 5)
    nt.assert_equals(x+y, z)


def test_str():
    x = Vector(1, 2)
    xs = 'Vector(1, 2)'


def test_len():
    x = Vector(1, 2)
    nt.assert_equals(len(x), 2)


def test_scalar_mult():
    x = Vector(1, 2)
    y1 = 2*x
    y2 = x*2
    z = Vector(2, 4)
    nt.assert_equals(y1, z)
    nt.assert_equals(y2, z)


def test_dot_product():
    x = Vector(1, 2)
    y = Vector(2, 4)
    nt.assert_equals(x*y, 10)
