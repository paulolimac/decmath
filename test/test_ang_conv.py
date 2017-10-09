# Import namespaces and helper functions from __init__.py
import math as m
import decmath as dm

from test import abteq


def test_degrees():
    assert abteq(dm.degrees(.5), m.degrees(.5))
    assert abteq(dm.degrees(7.1), m.degrees(7.1))
    assert abteq(dm.degrees(-.5), m.degrees(-.5))
    assert abteq(dm.degrees(-7.1), m.degrees(-7.1))
    assert dm.degrees(dm.pi) == 180
    assert dm.degrees(dm.pi / 2), 90


def test_radians():
    assert abteq(dm.radians(.5), m.radians(.5))
    assert abteq(dm.radians(7.1), m.radians(7.1))
    assert abteq(dm.radians(-.5), m.radians(-.5))
    assert abteq(dm.radians(-7.1), m.radians(-7.1))
    assert dm.radians(180) == dm.pi
    assert dm.radians(90) == dm.pi / 2
