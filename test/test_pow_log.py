# Import namespaces and helper functions from __init__.py
from test import *

def test_exp():
    assert dm.exp(1) == dm.e
    assert abteq(dm.exp(.7), m.exp(.7))

def test_expm1():
    assert dm.expm1(1) == dm.e - 1
    assert abteq(dm.expm1(.7), m.expm1(.7))

def test_log():
    assert msteq(dm.log(dm.e), 1) # This isn't exact!
    assert dm.log(100, 10) == 2
    assert abteq(dm.log(3, 4), m.log(3, 4))

def test_log1p():
    assert msteq(dm.log1p(dm.e - 1), 1) # This isn't exact!
    assert abteq(dm.log1p(3), m.log1p(3))

def test_log2():
    assert dm.log2(4) == 2
    assert abteq(dm.log2(8.9), m.log2(8.9))

def test_log10():
    assert dm.log10(100) == 2
    assert abteq(dm.log10(8.9), m.log10(8.9))

def test_pow():
    assert dm.pow(2, 2) == 4
    assert dm.pow(2, -2) == D(1/4)
    assert dm.pow(4, 1/2) == 2
    assert abteq(dm.pow(3.4, 5.6), m.pow(3.4, 5.6))

def test_sqrt():
    assert dm.sqrt(4) == 2
    assert dm.sqrt(dm.exp(2)) == dm.e
    assert abteq(dm.sqrt(4.2), m.sqrt(4.2))
