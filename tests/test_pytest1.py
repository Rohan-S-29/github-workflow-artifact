import math
import pytest

def test_add():
    assert math.add(2, 3) == 5

def test_subtract():
    assert math.subtract(10, 5) == 5

def test_multiply():
    assert math.multiply(4, 5) == 20

def test_divide():
    assert math.divide(10, 2) == 5
