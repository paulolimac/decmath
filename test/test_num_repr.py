# Import namespaces and helper functions from __init__.py
import math as m
import decmath as dm
import pytest as pt

from decimal import Decimal

from test import abteq


def test_ceil():
    assert dm.ceil(-1) == -1
    assert dm.ceil(-0) == -0
    assert dm.ceil(-0) == 0
    assert dm.ceil(-0) == +0
    assert dm.ceil(0) == -0
    assert dm.ceil(0) == 0
    assert dm.ceil(0) == +0
    assert dm.ceil(+0) == -0
    assert dm.ceil(+0) == 0
    assert dm.ceil(+0) == +0
    assert dm.ceil(1) == 1
    assert dm.ceil(-1.1) == -1
    assert dm.ceil(-0.0) == -0
    assert dm.ceil(-0.0) == 0
    assert dm.ceil(-0.0) == +0
    assert dm.ceil(0.0) == -0
    assert dm.ceil(0.0) == 0
    assert dm.ceil(0.0) == +0
    assert dm.ceil(+0.0) == -0
    assert dm.ceil(+0.0) == 0
    assert dm.ceil(+0.0) == +0
    assert dm.ceil(0.1) == 1
    assert dm.ceil(.1) == 1
    assert dm.ceil(1.1) == 2
    assert abteq(dm.ceil(-1), m.ceil(-1))
    assert abteq(dm.ceil(-0), m.ceil(-0))
    assert abteq(dm.ceil(0), m.ceil(0))
    assert abteq(dm.ceil(+0), m.ceil(+0))
    assert abteq(dm.ceil(1), m.ceil(1))
    assert abteq(dm.ceil(-1.1), m.ceil(-1.1))
    assert abteq(dm.ceil(-0.0), m.ceil(-0.0))
    assert abteq(dm.ceil(0.0), m.ceil(0.0))
    assert abteq(dm.ceil(+0.0), m.ceil(+0.0))
    assert abteq(dm.ceil(0.1), m.ceil(0.1))
    assert abteq(dm.ceil(.1), m.ceil(.1))
    assert abteq(dm.ceil(1.1), m.ceil(1.1))
    #assert pt.raises(ValueError, "dm.ceil('A')")
    assert m.isnan(dm.ceil(Decimal('NaN')))


def test_copysign():
    assert dm.copysign(-1,-1) == -1
    assert dm.copysign(-1,1) == 1
    assert dm.copysign(-1,1) == +1
    assert dm.copysign(-1,+1) == 1
    assert dm.copysign(-1,+1) == +1
    #assert dm.copysign(-1,-0) == -1
    assert dm.copysign(-1,0) == 1
    assert dm.copysign(-1,0) == +1
    assert dm.copysign(-1,+0) == +1
    assert dm.copysign(-1,+0) == 1
    assert dm.copysign(-0,-1) == -0
    assert dm.copysign(-0,-1) == 0
    assert dm.copysign(-0,-1) == +0
    assert dm.copysign(-0,1) == -0
    assert dm.copysign(-0,1) == 0
    assert dm.copysign(-0,1) == +0
    assert dm.copysign(-0,+1) == -0
    assert dm.copysign(-0,+1) == 0
    assert dm.copysign(-0,+1) == +0
    assert dm.copysign(-0,-0) == -0
    assert dm.copysign(-0,0) == 0
    assert dm.copysign(-0,+0) == +0
    assert dm.copysign(0,-1) == -0
    assert dm.copysign(0,-1) == 0
    assert dm.copysign(0,-1) == +0
    assert dm.copysign(0,1) == -0
    assert dm.copysign(0,1) == 0
    assert dm.copysign(0,1) == +0
    assert dm.copysign(0,+1) == -0
    assert dm.copysign(0,+1) == 0
    assert dm.copysign(0,+1) == +0
    assert dm.copysign(0,-0) == -0
    assert dm.copysign(0,0) == 0
    assert dm.copysign(0,+0) == +0
    assert dm.copysign(+0,-1) == -0
    assert dm.copysign(+0,-1) == 0
    assert dm.copysign(+0,-1) == +0
    assert dm.copysign(+0,1) == -0
    assert dm.copysign(+0,1) == 0
    assert dm.copysign(+0,1) == +0
    assert dm.copysign(+0,+1) == -0
    assert dm.copysign(+0,+1) == 0
    assert dm.copysign(+0,+1) == +0
    assert dm.copysign(+0,-0) == -0
    assert dm.copysign(+0,0) == 0
    assert dm.copysign(+0,+0) == +0
    assert dm.copysign(1,-1) == -1
    assert dm.copysign(1,1) == 1
    assert dm.copysign(1,1) == +1
    assert dm.copysign(1,+1) == 1
    assert dm.copysign(1,+1) == +1
    #assert dm.copysign(1,-0) == -1
    assert dm.copysign(1,0) == 1
    assert dm.copysign(1,0) == +1
    assert dm.copysign(1,+0) == +1
    assert dm.copysign(1,+0) == 1
    assert dm.copysign(+1,-1) == -1
    assert dm.copysign(+1,1) == 1
    assert dm.copysign(+1,1) == +1
    assert dm.copysign(+1,+1) == 1
    assert dm.copysign(+1,+1) == +1
    #assert dm.copysign(+1,-0) == -1
    assert dm.copysign(+1,0) == 1
    assert dm.copysign(+1,0) == +1
    assert dm.copysign(+1,+0) == +1
    assert dm.copysign(+1,+0) == 1
    assert dm.copysign(-1.0,-1.0) == -1.0
    assert dm.copysign(-1.0,1.0) == 1.0
    assert dm.copysign(-1.0,1.0) == +1.0
    assert dm.copysign(-1.0,+1.0) == 1.0
    assert dm.copysign(-1.0,+1.0) == +1.0
    #assert dm.copysign(-1.0,-0.0) == -1.0
    assert dm.copysign(-1.0,0.0) == 1.0
    assert dm.copysign(-1.0,0.0) == +1.0
    assert dm.copysign(-1.0,+0.0) == +1.0
    assert dm.copysign(-1.0,+0.0) == 1.0
    assert dm.copysign(-0.0,-1.0) == -0.0
    assert dm.copysign(-0.0,-1.0) == 0.0
    assert dm.copysign(-0.0,-1.0) == +0.0
    assert dm.copysign(-0.0,1.0) == -0.0
    assert dm.copysign(-0.0,1.0) == 0.0
    assert dm.copysign(-0.0,1.0) == +0.0
    assert dm.copysign(-0.0,+1.0) == -0.0
    assert dm.copysign(-0.0,+1.0) == 0.0
    assert dm.copysign(-0.0,+1.0) == +0.0
    assert dm.copysign(-0.0,-0.0) == -0.0
    assert dm.copysign(-0.0,0.0) == 0.0
    assert dm.copysign(-0.0,+0.0) == +0.0
    assert dm.copysign(0.0,-1.0) == -0.0
    assert dm.copysign(0.0,-1.0) == 0.0
    assert dm.copysign(0.0,-1.0) == +0.0
    assert dm.copysign(0.0,1.0) == -0.0
    assert dm.copysign(0.0,1.0) == 0.0
    assert dm.copysign(0.0,1.0) == +0.0
    assert dm.copysign(0.0,+1.0) == -0.0
    assert dm.copysign(0.0,+1.0) == 0.0
    assert dm.copysign(0.0,+1.0) == +0.0
    assert dm.copysign(0.0,-0.0) == -0.0
    assert dm.copysign(0.0,0.0) == 0.0
    assert dm.copysign(0.0,+0.0) == +0.0
    assert dm.copysign(+0.0,-1.0) == -0.0
    assert dm.copysign(+0.0,-1.0) == 0.0
    assert dm.copysign(+0.0,-1.0) == +0.0
    assert dm.copysign(+0.0,1.0) == -0.0
    assert dm.copysign(+0.0,1.0) == 0.0
    assert dm.copysign(+0.0,1.0) == +0.0
    assert dm.copysign(+0.0,+1.0) == -0.0
    assert dm.copysign(+0.0,+1.0) == 0.0
    assert dm.copysign(+0.0,+1.0) == +0.0
    assert dm.copysign(+0.0,-0.0) == -0.0
    assert dm.copysign(+0.0,0.0) == 0.0
    assert dm.copysign(+0.0,+0.0) == +0.0
    assert dm.copysign(1.0,-1.0) == -1.0
    assert dm.copysign(1.0,1.0) == 1.0
    assert dm.copysign(1.0,1.0) == +1.0
    assert dm.copysign(1.0,+1.0) == 1.0
    assert dm.copysign(1.0,+1.0) == +1.0
    #assert dm.copysign(1.0,-0.0) == -1.0
    assert dm.copysign(1.0,0.0) == 1.0
    assert dm.copysign(1.0,0.0) == +1.0
    assert dm.copysign(1.0,+0.0) == +1.0
    assert dm.copysign(1.0,+0.0) == 1.0
    assert dm.copysign(+1.0,-1.0) == -1.0
    assert dm.copysign(+1.0,1.0) == 1.0
    assert dm.copysign(+1.0,1.0) == +1.0
    assert dm.copysign(+1.0,+1.0) == 1.0
    assert dm.copysign(+1.0,+1.0) == +1.0
    #assert dm.copysign(+1.0,-0.0) == -1.0
    assert dm.copysign(+1.0,0.0) == 1.0
    assert dm.copysign(+1.0,0.0) == +1.0
    assert dm.copysign(+1.0,+0.0) == +1.0
    assert dm.copysign(+1.0,+0.0) == 1.0
    assert abteq(dm.copysign(-1,-1),m.copysign(-1,-1))
    assert abteq(dm.copysign(-1,1),m.copysign(-1,1))
    assert abteq(dm.copysign(-1,+1),m.copysign(-1,+1))
    #assert abteq(dm.copysign(-1,-0),m.copysign(-1,-0))
    assert abteq(dm.copysign(-1,0),m.copysign(-1,0))
    assert abteq(dm.copysign(-1,+0),m.copysign(-1,+0))
    assert abteq(dm.copysign(-0,-1),m.copysign(-0,-1))
    assert abteq(dm.copysign(-0,1),m.copysign(-0,1))
    assert abteq(dm.copysign(-0,+1),m.copysign(-0,+1))
    #assert abteq(dm.copysign(-0,-0),m.copysign(-0,-0))
    assert abteq(dm.copysign(-0,0),m.copysign(-0,0))
    assert abteq(dm.copysign(-0,+0),m.copysign(-0,+0))
    assert abteq(dm.copysign(1,-1),m.copysign(1,-1))
    assert abteq(dm.copysign(1,1),m.copysign(1,1))
    assert abteq(dm.copysign(1,+1),m.copysign(1,+1))
    #assert abteq(dm.copysign(1,-0),m.copysign(1,-0))
    assert abteq(dm.copysign(1,0),m.copysign(1,0))
    assert abteq(dm.copysign(1,+0),m.copysign(1,+0))
    assert abteq(dm.copysign(+1,-1),m.copysign(+1,-1))
    assert abteq(dm.copysign(+1,1),m.copysign(+1,1))
    assert abteq(dm.copysign(+1,+1),m.copysign(+1,+1))
    #assert abteq(dm.copysign(+1,-0),m.copysign(+1,-0))
    assert abteq(dm.copysign(+1,0),m.copysign(+1,0))
    assert abteq(dm.copysign(+1,+0),m.copysign(+1,+0))
    assert abteq(dm.copysign(-1,Decimal('NaN')),m.copysign(-1,Decimal('NaN')))
    assert abteq(dm.copysign(-1,Decimal('NaN')),m.copysign(-1,Decimal('NaN')))
    assert abteq(dm.copysign(-0,Decimal('NaN')),m.copysign(-0,Decimal('NaN')))
    assert abteq(dm.copysign(-0,Decimal('NaN')),m.copysign(-0,Decimal('NaN')))
    assert abteq(dm.copysign(-0,Decimal('NaN')),m.copysign(-0,Decimal('NaN')))
    assert abteq(dm.copysign(0,Decimal('NaN')),m.copysign(0,Decimal('NaN')))
    assert abteq(dm.copysign(0,Decimal('NaN')),m.copysign(0,Decimal('NaN')))
    assert abteq(dm.copysign(0,Decimal('NaN')),m.copysign(0,Decimal('NaN')))
    assert abteq(dm.copysign(+0,Decimal('NaN')),m.copysign(+0,Decimal('NaN')))
    assert abteq(dm.copysign(+0,Decimal('NaN')),m.copysign(+0,Decimal('NaN')))
    assert abteq(dm.copysign(+0,Decimal('NaN')),m.copysign(+0,Decimal('NaN')))
    assert abteq(dm.copysign(1,Decimal('NaN')),m.copysign(1,Decimal('NaN')))
    assert abteq(dm.copysign(+1,Decimal('NaN')),m.copysign(+1,Decimal('NaN')))
    assert abteq(dm.copysign(-1.0,-1.0),m.copysign(-1.0,-1.0))
    assert abteq(dm.copysign(-1.0,1.0),m.copysign(-1.0,1.0))
    assert abteq(dm.copysign(-1.0,+1.0),m.copysign(-1.0,+1.0))
    #assert abteq(dm.copysign(-1.0,-0.0),m.copysign(-1,-0))
    assert abteq(dm.copysign(-1.0,0.0),m.copysign(-1.0,0.0))
    assert abteq(dm.copysign(-1.0,+0.0),m.copysign(-1.0,+0.0))
    assert abteq(dm.copysign(-0.0,-1.0),m.copysign(-0.0,-1.0))
    assert abteq(dm.copysign(-0.0,1.0),m.copysign(-0.0,1.0))
    assert abteq(dm.copysign(-0.0,+1.0),m.copysign(-0.0,+1.0))
    #assert abteq(dm.copysign(-0.0,-0.0),m.copysign(-0,-0))
    assert abteq(dm.copysign(-0.0,0.0),m.copysign(-0.0,0.0))
    assert abteq(dm.copysign(-0.0,+0.0),m.copysign(-0.0,+0.0))
    assert abteq(dm.copysign(1.0,-1.0),m.copysign(1.0,-1.0))
    assert abteq(dm.copysign(1.0,1.0),m.copysign(1.0,1.0))
    assert abteq(dm.copysign(1.0,+1.0),m.copysign(1.0,+1.0))
    #assert abteq(dm.copysign(1.0,-0.0),m.copysign(1.0,-0.0))
    assert abteq(dm.copysign(1.0,0.0),m.copysign(1.0,0.0))
    assert abteq(dm.copysign(1.0,+0.0),m.copysign(1.0,+0.0))
    assert abteq(dm.copysign(+1.0,-1.0),m.copysign(+1.0,-1.0))
    assert abteq(dm.copysign(+1.0,1.0),m.copysign(+1.0,1.0))
    assert abteq(dm.copysign(+1.0,+1.0),m.copysign(+1.0,+1.0))
    #assert abteq(dm.copysign(+1.0,-0.0),m.copysign(+1.0,-0.0))
    assert abteq(dm.copysign(+1.0,0.0),m.copysign(+1.0,0.0))
    assert abteq(dm.copysign(+1.0,+0.0),m.copysign(+1.0,+0.0))
    assert abteq(dm.copysign(-1.0,Decimal('NaN')),m.copysign(-1.0,Decimal('NaN')))
    assert abteq(dm.copysign(-1.0,Decimal('NaN')),m.copysign(-1.0,Decimal('NaN')))
    assert abteq(dm.copysign(-0.0,Decimal('NaN')),m.copysign(-0.0,Decimal('NaN')))
    assert abteq(dm.copysign(-0.0,Decimal('NaN')),m.copysign(-0.0,Decimal('NaN')))
    assert abteq(dm.copysign(-0.0,Decimal('NaN')),m.copysign(-0.0,Decimal('NaN')))
    assert abteq(dm.copysign(0.0,Decimal('NaN')),m.copysign(0.0,Decimal('NaN')))
    assert abteq(dm.copysign(0.0,Decimal('NaN')),m.copysign(0.0,Decimal('NaN')))
    assert abteq(dm.copysign(0.0,Decimal('NaN')),m.copysign(0.0,Decimal('NaN')))
    assert abteq(dm.copysign(+0.0,Decimal('NaN')),m.copysign(+0.0,Decimal('NaN')))
    assert abteq(dm.copysign(+0.0,Decimal('NaN')),m.copysign(+0.0,Decimal('NaN')))
    assert abteq(dm.copysign(+0.0,Decimal('NaN')),m.copysign(+0.0,Decimal('NaN')))
    assert abteq(dm.copysign(1.0,Decimal('NaN')),m.copysign(1.0,Decimal('NaN')))
    assert abteq(dm.copysign(+1.0,Decimal('NaN')),m.copysign(+1.0,Decimal('NaN')))
    assert dm.copysign(-1,Decimal('NaN')) == 1
    assert dm.copysign(-1,Decimal('NaN')) == +1
    assert dm.copysign(-0,Decimal('NaN')) == -0
    assert dm.copysign(-0,Decimal('NaN')) == 0
    assert dm.copysign(-0,Decimal('NaN')) == +0
    assert dm.copysign(0,Decimal('NaN')) == -0
    assert dm.copysign(0,Decimal('NaN')) == 0
    assert dm.copysign(0,Decimal('NaN')) == +0
    assert dm.copysign(+0,Decimal('NaN')) == -0
    assert dm.copysign(+0,Decimal('NaN')) == 0
    assert dm.copysign(+0,Decimal('NaN')) == +0
    assert dm.copysign(1,Decimal('NaN')) == 1
    assert dm.copysign(+1,Decimal('NaN')) == +1
    assert dm.copysign(-1.0,Decimal('NaN')) == 1.0
    assert dm.copysign(-1.0,Decimal('NaN')) == +1.0
    assert dm.copysign(-0.0,Decimal('NaN')) == -0.0
    assert dm.copysign(-0.0,Decimal('NaN')) == 0.0
    assert dm.copysign(-0.0,Decimal('NaN')) == +0.0
    assert dm.copysign(0.0,Decimal('NaN')) == -0.0
    assert dm.copysign(0.0,Decimal('NaN')) == 0.0
    assert dm.copysign(0.0,Decimal('NaN')) == +0.0
    assert dm.copysign(+0.0,Decimal('NaN')) == -0.0
    assert dm.copysign(+0.0,Decimal('NaN')) == 0.0
    assert dm.copysign(+0.0,Decimal('NaN')) == +0.0
    assert dm.copysign(1.0,Decimal('NaN')) == 1.0
    assert dm.copysign(+1.0,Decimal('NaN')) == +1.0
    #assert isinstance(dm.copysign(-1,-1),float)
    #assert isinstance(dm.copysign(-1,1),float)
    #assert isinstance(dm.copysign(-1,+1),float)
    #assert isinstance(dm.copysign(-1,-0),float)
    #assert isinstance(dm.copysign(-1,0),float)
    #assert isinstance(dm.copysign(-1,+0),float)
    #assert isinstance(dm.copysign(-0,-1),float)
    #assert isinstance(dm.copysign(-0,1),float)
    #assert isinstance(dm.copysign(-0,+1),float)
    #assert isinstance(dm.copysign(-0,-0),float)
    #assert isinstance(dm.copysign(-0,0),float)
    #assert isinstance(dm.copysign(-0,+0),float)
    #assert isinstance(dm.copysign(0,-1),float)
    #assert isinstance(dm.copysign(0,1),float)
    #assert isinstance(dm.copysign(0,+1),float)
    #assert isinstance(dm.copysign(0,-0),float)
    #assert isinstance(dm.copysign(0,0),float)
    #assert isinstance(dm.copysign(0,+0),float)
    #assert isinstance(dm.copysign(+0,-1),float)
    #assert isinstance(dm.copysign(+0,1),float)
    #assert isinstance(dm.copysign(+0,+1),float)
    #assert isinstance(dm.copysign(+0,-0),float)
    #assert isinstance(dm.copysign(+0,0),float)
    #assert isinstance(dm.copysign(+0,+0),float)
    #assert isinstance(dm.copysign(1,-1),float)
    #assert isinstance(dm.copysign(1,1),float)
    #assert isinstance(dm.copysign(1,+1),float)
    #assert isinstance(dm.copysign(1,-0),float)
    #assert isinstance(dm.copysign(1,0),float)
    #assert isinstance(dm.copysign(1,+0),float)
    #assert isinstance(dm.copysign(+1,-1),float)
    #assert isinstance(dm.copysign(+1,1),float)
    #assert isinstance(dm.copysign(+1,+1),float)
    #assert isinstance(dm.copysign(+1,-0),float)
    #assert isinstance(dm.copysign(+1,0),float)
    #assert isinstance(dm.copysign(+1,+0),float)
    #assert isinstance(dm.copysign(-1,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-1,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(1,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+1,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-1.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-1.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(-0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+0.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(1.0,Decimal('NaN')),float)
    #assert isinstance(dm.copysign(+1.0,Decimal('NaN')),float)
    #assert pt.raises(ValueError, "dm.copysign(0,'A')")
    #assert pt.raises(ValueError, "dm.copysign('A',0)")
    assert m.isnan(dm.copysign(Decimal('NaN'),-1))
    assert m.isnan(dm.copysign(Decimal('NaN'),1))
    assert m.isnan(dm.copysign(Decimal('NaN'),+1))
    assert m.isnan(dm.copysign(Decimal('NaN'),-0))
    assert m.isnan(dm.copysign(Decimal('NaN'),0))
    assert m.isnan(dm.copysign(Decimal('NaN'),+0))
    assert m.isnan(dm.copysign(Decimal('NaN'),-1.0))
    assert m.isnan(dm.copysign(Decimal('NaN'),1.0))
    assert m.isnan(dm.copysign(Decimal('NaN'),+1.0))
    assert m.isnan(dm.copysign(Decimal('NaN'),-0.0))
    assert m.isnan(dm.copysign(Decimal('NaN'),0.0))
    assert m.isnan(dm.copysign(Decimal('NaN'),+0.0))


def test_fabs():
    assert dm.fabs(-1) == 1
    assert dm.fabs(-0) == -0
    assert dm.fabs(-0) == 0
    assert dm.fabs(-0) == +0
    assert dm.fabs(0) == -0
    assert dm.fabs(0) == 0
    assert dm.fabs(0) == +0
    assert dm.fabs(+0) == -0
    assert dm.fabs(+0) == 0
    assert dm.fabs(+0) == +0
    assert dm.fabs(1) == 1
    assert abteq(dm.fabs(-1.1),1.1)
    assert dm.fabs(-0.0) == -0
    assert dm.fabs(-0.0) == 0
    assert dm.fabs(-0.0) == +0
    assert dm.fabs(0.0) == -0
    assert dm.fabs(0.0) == 0
    assert dm.fabs(0.0) == +0
    assert dm.fabs(+0.0) == -0
    assert dm.fabs(+0.0) == 0
    assert dm.fabs(+0.0) == +0
    assert abteq(dm.fabs(0.1),0.1)
    assert abteq(dm.fabs(.1),.1)
    assert abteq(dm.fabs(1.1),1.1)
    assert abteq(dm.fabs(-1), m.fabs(-1))
    assert abteq(dm.fabs(-0), m.fabs(-0))
    assert abteq(dm.fabs(0), m.fabs(0))
    assert abteq(dm.fabs(+0), m.fabs(+0))
    assert abteq(dm.fabs(1), m.fabs(1))
    assert abteq(dm.fabs(-1.1), m.fabs(-1.1))
    assert abteq(dm.fabs(-0.0), m.fabs(-0.0))
    assert abteq(dm.fabs(0.0), m.fabs(0.0))
    assert abteq(dm.fabs(+0.0), m.fabs(+0.0))
    assert abteq(dm.fabs(0.1), m.fabs(0.1))
    assert abteq(dm.fabs(.1), m.fabs(.1))
    assert abteq(dm.fabs(1.1), m.fabs(1.1))
    #assert pt.raises(ValueError, "dm.fabs('A')")
    assert m.isnan(dm.fabs(Decimal('NaN')))


def test_factorial():
    assert pt.raises(ValueError, "dm.factorial(-1)")
    assert dm.factorial(-0) == 1
    assert dm.factorial(0) == 1
    assert dm.factorial(+0) == 1
    assert dm.factorial(1) == 1
    assert pt.raises(ValueError, "dm.factorial(-1.0)")
    assert dm.factorial(-0.0) == 1
    assert dm.factorial(0.0) == 1
    assert dm.factorial(+0.0) == 1
    assert pt.raises(ValueError, "dm.factorial(0.1)")
    assert pt.raises(ValueError, "dm.factorial(.1)")
    assert pt.raises(ValueError, "dm.factorial(1.1)")
    assert abteq(dm.factorial(-0), m.factorial(-0))
    assert abteq(dm.factorial(0), m.factorial(0))
    assert abteq(dm.factorial(+0), m.factorial(+0))
    assert abteq(dm.factorial(1), m.factorial(1))
    assert abteq(dm.factorial(-0.0), m.factorial(-0.0))
    assert abteq(dm.factorial(0.0), m.factorial(0.0))
    assert abteq(dm.factorial(+0.0), m.factorial(+0.0))
    #assert pt.raises(ValueError, "dm.factorial('A')")
    assert pt.raises(ValueError, "dm.factorial(Decimal('NaN'))")
    

def test_floor():
    assert dm.floor(-1) == -1
    assert dm.floor(-0) == -0
    assert dm.floor(-0) == 0
    assert dm.floor(-0) == +0
    assert dm.floor(0) == -0
    assert dm.floor(0) == 0
    assert dm.floor(0) == +0
    assert dm.floor(+0) == -0
    assert dm.floor(+0) == 0
    assert dm.floor(+0) == +0
    assert dm.floor(1) == 1
    assert dm.floor(-1.1) == -2
    assert dm.floor(-0.0) == -0
    assert dm.floor(-0.0) == 0
    assert dm.floor(-0.0) == +0
    assert dm.floor(0.0) == -0
    assert dm.floor(0.0) == 0
    assert dm.floor(0.0) == +0
    assert dm.floor(+0.0) == -0
    assert dm.floor(+0.0) == 0
    assert dm.floor(+0.0) == +0
    assert dm.floor(0.1) == -0
    assert dm.floor(0.1) == 0
    assert dm.floor(0.1) == +0
    assert dm.floor(.1) == -0
    assert dm.floor(.1) == 0
    assert dm.floor(.1) == +0
    assert dm.floor(1.1) == 1
    assert abteq(dm.floor(-1), m.floor(-1))
    assert abteq(dm.floor(-0), m.floor(-0))
    assert abteq(dm.floor(0), m.floor(0))
    assert abteq(dm.floor(+0), m.floor(+0))
    assert abteq(dm.floor(1), m.floor(1))
    assert abteq(dm.floor(-1.1), m.floor(-1.1))
    assert abteq(dm.floor(-0.0), m.floor(-0.0))
    assert abteq(dm.floor(0.0), m.floor(0.0))
    assert abteq(dm.floor(+0.0), m.floor(+0.0))
    assert abteq(dm.floor(0.1), m.floor(0.1))
    assert abteq(dm.floor(.1), m.floor(.1))
    assert abteq(dm.floor(1.1), m.floor(1.1))
    #assert pt.raises(ValueError, "dm.floor('A')")
    assert m.isnan(dm.floor(Decimal('NaN')))


def test_fmod():
    assert dm.fmod(-1,-1) == 0
    assert dm.fmod(-1,1) == 0
    assert dm.fmod(-1,+1) == 0
    #assert pt.raises(ValueError, "dm.fmod(-1,0)")
    assert dm.fmod(1,-1) == 0
    assert dm.fmod(1,1) == 0
    assert dm.fmod(1,+1) == 0
    #assert pt.raises(ValueError, "dm.fmod(1,0)")
    assert dm.fmod(+1,-1) == 0
    assert dm.fmod(+1,1) == 0
    assert dm.fmod(+1,+1) == 0
    #assert pt.raises(ValueError, "dm.fmod(+1,0)")    
    #assert pt.raises(ValueError, "dm.fmod(-0,-0)")
    #assert pt.raises(ValueError, "dm.fmod(-0,0)")
    #assert pt.raises(ValueError, "dm.fmod(-0,+0)")
    #assert pt.raises(ValueError, "dm.fmod(0,-0)")
    #assert pt.raises(ValueError, "dm.fmod(0,0)")
    #assert pt.raises(ValueError, "dm.fmod(0,+0)")
    #assert pt.raises(ValueError, "dm.fmod(+0,-0)")
    #assert pt.raises(ValueError, "dm.fmod(+0,0)")
    #assert pt.raises(ValueError, "dm.fmod(+0,+0)")
    assert dm.fmod(0,-1) == 0
    assert dm.fmod(0,1) == 0
    assert dm.fmod(0,+1) == 0
    assert dm.fmod(-3,-1) == 0
    assert dm.fmod(-3,1) == 0
    assert dm.fmod(-3,+1) == 0
    assert dm.fmod(3,-1) == 0
    assert dm.fmod(3,1) == 0
    assert dm.fmod(3,+1) == 0
    assert dm.fmod(+3,-1) == 0
    assert dm.fmod(+3,1) == 0
    assert dm.fmod(+3,+1) == 0
    assert dm.fmod(-1,-3) == -1
    assert dm.fmod(-1,3) == -1
    assert dm.fmod(-1,+3) == -1
    assert dm.fmod(1,-3) == 1
    assert dm.fmod(1,3) == 1
    assert dm.fmod(1,+3) == 1
    assert dm.fmod(+1,-3) == 1
    assert dm.fmod(+1,3) == 1
    assert dm.fmod(+1,+3) == 1
    assert dm.fmod(-3,-2) == 1
    assert dm.fmod(-3,2) == 1
    assert dm.fmod(-3,+2) == 1
    assert dm.fmod(3,-2) == -1
    #assert dm.fmod(3,2) == -1
    #assert dm.fmod(3,+2) == -1
    assert dm.fmod(+3,-2) == -1
    #assert dm.fmod(+3,2) == -1
    #assert dm.fmod(+3,+2) == -1
    assert dm.fmod(-2,-3) == 1
    assert dm.fmod(-2,3) == 1
    assert dm.fmod(-2,+3) == 1
    assert dm.fmod(2,-3) == -1
    #assert dm.fmod(2,3) == -1
    #assert dm.fmod(2,+3) == -1
    assert dm.fmod(+2,-3) == -1
    #assert dm.fmod(+2,3) == -1
    #assert dm.fmod(+2,+3) == -1
    assert dm.fmod(-4,-2) == 0
    assert dm.fmod(-4,2) == 0
    assert dm.fmod(-4,+2) == 0
    assert dm.fmod(4,-2) == 0
    assert dm.fmod(4,2) == 0
    assert dm.fmod(4,+2) == 0
    assert dm.fmod(+4,-2) == 0
    assert dm.fmod(+4,2) == 0
    assert dm.fmod(+4,+2) == 0
    assert dm.fmod(-2,-4) == -2
    assert dm.fmod(-2,4) == -2
    assert dm.fmod(-2,+4) == -2
    assert dm.fmod(2,-4) == 2
    assert dm.fmod(2,4) == 2
    assert dm.fmod(2,+4) == 2
    assert dm.fmod(+2,-4) == 2
    assert dm.fmod(+2,4) == 2
    assert dm.fmod(+2,+4) == 2
    assert dm.fmod(-1.0,-1.0) == 0
    assert dm.fmod(-1.0,1.0) == 0
    assert dm.fmod(-1.0,+1.0) == 0
    #assert pt.raises(ValueError, "dm.fmod(-1.0,0.0)")
    assert dm.fmod(1.0,-1.0) == 0
    assert dm.fmod(1.0,1.0) == 0
    assert dm.fmod(1.0,+1.0) == 0
    #assert pt.raises(ValueError, "dm.fmod(1.0,0.0)")
    assert dm.fmod(+1.0,-1.0) == 0
    assert dm.fmod(+1.0,1.0) == 0
    assert dm.fmod(+1.0,+1.0) == 0
    #assert pt.raises(ValueError, "dm.fmod(+1.0,0.0)")
    assert dm.fmod(-4.0,-2.0) == 0
    assert dm.fmod(-4.0,2.0) == 0
    assert dm.fmod(-4.0,+2.0) == 0
    assert dm.fmod(4.0,-2.0) == 0
    assert dm.fmod(4.0,2.0) == 0
    assert dm.fmod(4.0,+2.0) == 0
    assert dm.fmod(+4.0,-2.0) == 0
    assert dm.fmod(+4.0,2.0) == 0
    assert dm.fmod(+4.0,+2.0) == 0
    assert dm.fmod(-2.0,-4.0) == -2
    assert dm.fmod(-2.0,4.0) == -2
    assert dm.fmod(-2.0,+4.0) == -2
    assert dm.fmod(2.0,-4.0) == 2
    assert dm.fmod(2.0,4.0) == 2
    assert dm.fmod(2.0,+4.0) == 2
    assert dm.fmod(+2.0,-4.0) == 2
    assert dm.fmod(+2.0,4.0) == 2
    assert dm.fmod(+2.0,+4.0) == 2
    assert dm.fmod(-0.4,-0.2) == 0
    assert dm.fmod(-0.4,0.2) == 0
    assert dm.fmod(-0.4,+0.2) == 0
    assert dm.fmod(0.4,-0.2) == 0
    assert dm.fmod(0.4,0.2) == 0
    assert dm.fmod(0.4,+0.2) == 0
    assert dm.fmod(+0.4,-0.2) == 0
    assert dm.fmod(+0.4,0.2) == 0
    assert dm.fmod(+0.4,+0.2) == 0
    assert dm.fmod(-0.2,-0.4) == Decimal('-0.2')
    assert dm.fmod(-0.2,0.4) == Decimal('-0.2')
    assert dm.fmod(-0.2,+0.4) == Decimal('-0.2')
    assert dm.fmod(0.2,-0.4) == Decimal('0.2')
    assert dm.fmod(0.2,0.4) == Decimal('0.2')
    assert dm.fmod(0.2,+0.4) == Decimal('0.2')
    assert dm.fmod(+0.2,-0.4) == Decimal('0.2')
    assert dm.fmod(+0.2,0.4) == Decimal('0.2')
    assert dm.fmod(+0.2,+0.4) == Decimal('0.2')
    assert abteq(dm.fmod(-4,-2),m.fmod(-4,-2))
    assert abteq(dm.fmod(-4,2),m.fmod(-4,2))
    assert abteq(dm.fmod(-4,+2),m.fmod(-4,+2))
    assert abteq(dm.fmod(4,-2),m.fmod(4,-2))
    assert abteq(dm.fmod(4,2),m.fmod(4,2))
    assert abteq(dm.fmod(4,+2),m.fmod(4,+2))
    assert abteq(dm.fmod(+4,-2),m.fmod(+4,-2))
    assert abteq(dm.fmod(+4,2),m.fmod(+4,2))
    assert abteq(dm.fmod(+4,+2),m.fmod(+4,+2))
    assert abteq(dm.fmod(-2,-4),m.fmod(-2,-4))
    assert abteq(dm.fmod(-2,4),m.fmod(-2,4))
    assert abteq(dm.fmod(-2,+4),m.fmod(-2,+4))
    assert abteq(dm.fmod(2,-4),m.fmod(2,-4))
    assert abteq(dm.fmod(2,4),m.fmod(2,4))
    assert abteq(dm.fmod(2,+4),m.fmod(2,+4))
    assert abteq(dm.fmod(+2,-4),m.fmod(+2,-4))
    assert abteq(dm.fmod(+2,4),m.fmod(+2,4))
    assert abteq(dm.fmod(+2,+4),m.fmod(+2,+4))
    assert abteq(dm.fmod(-0.4,-0.2),m.fmod(-0.4,-0.2))
    assert abteq(dm.fmod(-0.4,0.2),m.fmod(-0.4,0.2))
    assert abteq(dm.fmod(-0.4,+0.2),m.fmod(-0.4,+0.2))
    assert abteq(dm.fmod(0.4,-0.2),m.fmod(0.4,-0.2))
    assert abteq(dm.fmod(0.4,0.2),m.fmod(0.4,0.2))
    assert abteq(dm.fmod(0.4,+0.2),m.fmod(0.4,+0.2))
    assert abteq(dm.fmod(+0.4,-0.2),m.fmod(+0.4,-0.2))
    assert abteq(dm.fmod(+0.4,0.2),m.fmod(+0.4,0.2))
    assert abteq(dm.fmod(+0.4,+0.2),m.fmod(+0.4,+0.2))
    assert abteq(dm.fmod(-0.2,-0.4),m.fmod(-0.2,-0.4))
    assert abteq(dm.fmod(-0.2,0.4),m.fmod(-0.2,0.4))
    assert abteq(dm.fmod(-0.2,+0.4),m.fmod(-0.2,+0.4))
    assert abteq(dm.fmod(0.2,-0.4),m.fmod(0.2,-0.4))
    assert abteq(dm.fmod(0.2,0.4),m.fmod(0.2,0.4))
    assert abteq(dm.fmod(0.2,+0.4),m.fmod(0.2,+0.4))
    assert abteq(dm.fmod(+0.2,-0.4),m.fmod(+0.2,-0.4))
    assert abteq(dm.fmod(+0.2,0.4),m.fmod(+0.2,0.4))
    assert abteq(dm.fmod(+0.2,+0.4),m.fmod(+0.2,+0.4))
    #assert pt.raises(ValueError, "dm.fmod('A',1)")
    #assert pt.raises(ValueError, "dm.fmod(1,'A')")
    assert m.isnan(dm.fmod(Decimal('NaN'),2))
    assert m.isnan(dm.fmod(2,Decimal('NaN')))


def test_frexp():
    assert dm.frexp(-1) == (Decimal('-0.5'), 1)
    assert dm.frexp(-0) == (Decimal('-0.0'), 0)
    assert dm.frexp(0) == (Decimal('-0.0'), 0)
    assert dm.frexp(+0) == (Decimal('-0.0'), 0)
    assert dm.frexp(1) == (Decimal('0.5'), 1)
    assert dm.frexp(-1.1) == (Decimal('-0.55'), 1)
    assert dm.frexp(-0.0) == (Decimal('-0.0'), 0)
    assert dm.frexp(0.0) == (Decimal('-0.0'), 0)
    assert dm.frexp(+0.0) == (Decimal('-0.0'), 0)
    assert dm.frexp(0.1) == (Decimal('0.8'), -3)
    assert dm.frexp(.1) == (Decimal('0.8'), -3)
    assert dm.frexp(1.1) == (Decimal('0.55'), 1)
    assert dm.frexp(-1) == m.frexp(-1)
    assert dm.frexp(-0) == m.frexp(-0)
    assert dm.frexp(0) == m.frexp(0)
    assert dm.frexp(+0) == m.frexp(+0)
    assert dm.frexp(1) == m.frexp(1)
    #assert dm.frexp(-1.1) == m.frexp(-1.1)
    assert dm.frexp(-0.0) == m.frexp(-0.0)
    assert dm.frexp(0.0) == m.frexp(0.0)
    assert dm.frexp(+0.0) == m.frexp(+0.0)
    #assert dm.frexp(0.1) == m.frexp(0.1)
    #assert dm.frexp(.1) == m.frexp(.1)
    #assert dm.frexp(1.1) == m.frexp(1.1)
    #assert pt.raises(ValueError, "dm.frexp('A')")
    #assert m.isnan(dm.frexp(Decimal('NaN')))
    


#def test_fsum():


#def test_gcd():


#def test_isclose():


#def test_ldexp():


#def test_modf():


#def test_remainder():


#def test_sign():


#def test_signt():

