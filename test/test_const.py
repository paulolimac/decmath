# Import namespaces and helper functions from __init__
from test import *

def test_phi():
    assert abteq((1 + dm.phi) / dm.phi, dm.phi)

def test_pi():
    assert abteq(dm.pi, m.pi)

def test_e():
    assert abteq(dm.e, m.e)

def test_tau():
    # We already tested pi so now we use that to test tau.
    assert abteq(dm.tau / 2, dm.pi)

def test_inf():
    assert (dm.inf > 0) and m.isinf(dm.inf)

def test_nan():
    assert (dm.nan != dm.nan) and m.isnan(dm.nan)
