# Import namespaces and helper functions from __init__.py
from test import *

def test_acos():
    assert dm.acos(-1) == dm.pi
    assert dm.acos(0) == dm.pi/2
    assert dm.acos(1) == 0
    assert abteq(dm.acos(.5), m.acos(.5))
    assert abteq(dm.acos(-.5), m.acos(-.5))
    assert pt.raises(ValueError, "dm.acos(1.1)")
    assert pt.raises(ValueError, "dm.acos(-1.1)")

def test_asin():
    assert dm.asin(-1) == -dm.pi/2
    assert dm.asin(0) == 0
    assert dm.asin(1) == dm.pi/2
    assert abteq(dm.asin(.5), m.asin(.5))
    assert abteq(dm.asin(-.5), m.asin(-.5))
    assert pt.raises(ValueError, "dm.asin(1.1)")
    assert pt.raises(ValueError, "dm.asin(-1.1)")

def test_atan():
    assert dm.atan(D("Inf")) == dm.pi/2
    assert dm.atan(D("-Inf")) == -dm.pi/2
    assert dm.atan(0) == 0
    assert abteq(dm.atan(.5), m.atan(.5))
    assert abteq(dm.atan(-.5), m.atan(-.5))

def test_atan2():
    assert abteq(dm.atan2(.5, .4), m.atan2(.5, .4))
    assert abteq(dm.atan2(-.6, .2), m.atan2(-.6, .2))
    assert abteq(dm.atan2(.3, -.4), m.atan2(.3, -.4))
    assert abteq(dm.atan2(-.8, -.2), m.atan2(-.8, -.2))
    assert abteq(dm.atan2(D("Inf"), .2), m.atan2(D("Inf"), .2))
    assert abteq(dm.atan2(D("-Inf"), .2), m.atan2(D("-Inf"), .2))
    assert abteq(dm.atan2(D("Inf"), -.2), m.atan2(D("Inf"), -.2))
    assert abteq(dm.atan2(D("-Inf"), -.2), m.atan2(D("-Inf"), -.2))
    assert abteq(dm.atan2(.2, D("Inf")), m.atan2(.2, D("Inf")))
    assert abteq(dm.atan2(-.2, D("Inf")), m.atan2(-.2, D("Inf")))
    assert abteq(dm.atan2(.2, D("-Inf")), m.atan2(.2, D("-Inf")))
    assert abteq(dm.atan2(-.2, D("-Inf")), m.atan2(-.2, D("-Inf")))
    assert abteq(dm.atan2(D("Inf"), D("Inf")), m.atan2(D("Inf"), D("Inf")))
    assert abteq(dm.atan2(D("-Inf"), D("Inf")), m.atan2(D("-Inf"), D("Inf")))
    assert abteq(dm.atan2(D("Inf"), D("-Inf")), m.atan2(D("Inf"), D("-Inf")))
    assert abteq(dm.atan2(D("-Inf"), D("-Inf")), m.atan2(D("-Inf"), D("-Inf")))

def test_cos():
    assert dm.cos(0) == 1
    assert dm.cos(dm.pi/2) == 0
    assert dm.cos(dm.pi) == -1
    assert dm.cos(3 * dm.pi/2) == 0
    assert abteq(dm.cos(3), m.cos(3))
    assert abteq(dm.cos(-5), m.cos(-5))

def test_hypot():
    assert dm.hypot(1, 1) == dm.sqrt(2)
    assert abteq(dm.hypot(.5, .4), m.hypot(.5, .4))
    assert abteq(dm.hypot(5, -4), m.hypot(5, -4))

def test_sin():
    assert dm.sin(0) == 0
    assert dm.sin(dm.pi/2) == 1
    assert dm.sin(dm.pi) == 0
    assert dm.sin(3 * dm.pi/2) == -1
    assert abteq(dm.sin(3), m.sin(3))
    assert abteq(dm.sin(-5), m.sin(-5))

def test_tan():
    assert dm.tan(0) == 0
    assert dm.tan(dm.pi/2) == D('Inf')
    assert dm.tan(dm.pi) == 0
    assert dm.tan(3 * dm.pi/2) == D('-Inf')
    assert abteq(dm.tan(3), m.tan(3))
    assert abteq(dm.tan(-5), m.tan(-5))