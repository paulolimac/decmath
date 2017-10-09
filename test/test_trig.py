# Import namespaces and helper functions from __init__.py
import math as m
import decmath as dm
import pytest as pt

from decimal import Decimal

from test import abteq


def test_acos():
    assert dm.acos(-1) == dm.pi
    assert dm.acos(0) == dm.pi / 2
    assert dm.acos(1) == 0
    assert abteq(dm.acos(.5), m.acos(.5))
    assert abteq(dm.acos(-.5), m.acos(-.5))
    assert pt.raises(ValueError, "dm.acos(1.1)")
    assert pt.raises(ValueError, "dm.acos(-1.1)")
    assert m.isnan(dm.acos(Decimal("NaN")))


def test_asin():
    assert dm.asin(-1) == -dm.pi / 2
    assert dm.asin(0) == 0
    assert dm.asin(1) == dm.pi / 2
    assert abteq(dm.asin(.5), m.asin(.5))
    assert abteq(dm.asin(-.5), m.asin(-.5))
    assert pt.raises(ValueError, "dm.asin(1.1)")
    assert pt.raises(ValueError, "dm.asin(-1.1)")
    assert m.isnan(dm.asin(Decimal("NaN")))


def test_atan():
    assert dm.atan(Decimal("Inf")) == dm.pi / 2
    assert dm.atan(Decimal("-Inf")) == -dm.pi / 2
    assert dm.atan(0) == 0
    assert abteq(dm.atan(.5), m.atan(.5))
    assert abteq(dm.atan(-.5), m.atan(-.5))
    assert m.isnan(dm.atan(Decimal("NaN")))


def test_atan2():
    assert abteq(dm.atan2(.5, .4), m.atan2(.5, .4))
    assert abteq(dm.atan2(-.6, .2), m.atan2(-.6, .2))
    assert abteq(dm.atan2(.3, -.4), m.atan2(.3, -.4))
    assert abteq(dm.atan2(-.8, -.2), m.atan2(-.8, -.2))
    assert abteq(dm.atan2(Decimal("Inf"), .2), m.atan2(Decimal("Inf"), .2))
    assert abteq(dm.atan2(Decimal("-Inf"), .2), m.atan2(Decimal("-Inf"), .2))
    assert abteq(dm.atan2(Decimal("Inf"), -.2), m.atan2(Decimal("Inf"), -.2))
    assert abteq(dm.atan2(Decimal("-Inf"), -.2), m.atan2(Decimal("-Inf"), -.2))
    assert abteq(dm.atan2(.2, Decimal("Inf")), m.atan2(.2, Decimal("Inf")))
    assert abteq(dm.atan2(-.2, Decimal("Inf")), m.atan2(-.2, Decimal("Inf")))
    assert abteq(dm.atan2(.2, Decimal("-Inf")), m.atan2(.2, Decimal("-Inf")))
    assert abteq(dm.atan2(-.2, Decimal("-Inf")), m.atan2(-.2, Decimal("-Inf")))
    assert abteq(
        dm.atan2(Decimal("Inf"), Decimal("Inf")),
        m.atan2(Decimal("Inf"), Decimal("Inf")))
    assert abteq(
        dm.atan2(Decimal("-Inf"), Decimal("Inf")),
        m.atan2(Decimal("-Inf"), Decimal("Inf")))
    assert abteq(
        dm.atan2(Decimal("Inf"), Decimal("-Inf")),
        m.atan2(Decimal("Inf"), Decimal("-Inf")))
    assert abteq(
        dm.atan2(Decimal("-Inf"), Decimal("-Inf")),
        m.atan2(Decimal("-Inf"), Decimal("-Inf")))
    assert abteq(dm.atan2(0, 0), m.atan2(0, 0))
    assert abteq(dm.atan2(0, Decimal("-0")), m.atan2(0, Decimal("-0")))
    assert m.isnan(dm.atan2(Decimal("NaN"), 1))
    assert m.isnan(dm.atan2(1, Decimal("NaN")))
    assert m.isnan(dm.atan2(Decimal("NaN"), Decimal("NaN")))


def test_cos():
    assert dm.cos(0) == 1
    assert dm.cos(dm.pi / 2) == 0
    assert dm.cos(dm.pi) == -1
    assert dm.cos(3 * dm.pi / 2) == 0
    assert abteq(dm.cos(3), m.cos(3))
    assert abteq(dm.cos(-5), m.cos(-5))
    assert m.isnan(dm.cos(Decimal("NaN")))


def test_hypot():
    assert dm.hypot(1, 1) == dm.sqrt(2)
    assert abteq(dm.hypot(.5, .4), m.hypot(.5, .4))
    assert abteq(dm.hypot(5, -4), m.hypot(5, -4))


def test_sin():
    assert dm.sin(0) == 0
    assert dm.sin(dm.pi / 2) == 1
    assert dm.sin(dm.pi) == 0
    assert dm.sin(3 * dm.pi / 2) == -1
    assert abteq(dm.sin(3), m.sin(3))
    assert abteq(dm.sin(-5), m.sin(-5))
    assert m.isnan(dm.sin(Decimal("NaN")))


def test_tan():
    assert dm.tan(0) == 0
    assert dm.tan(dm.pi / 2) == Decimal('Inf')
    assert dm.tan(dm.pi) == 0
    assert dm.tan(3 * dm.pi / 2) == Decimal('-Inf')
    assert abteq(dm.tan(3), m.tan(3))
    assert abteq(dm.tan(-5), m.tan(-5))
    assert m.isnan(dm.tan(Decimal("NaN")))
