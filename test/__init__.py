import sys 
sys.path.append('..')

import decmath as dm
import math as m
import pytest as pt
from decimal import Decimal as D

def abteq(a, b):
    QF = D(10) ** -12 # This is the precission of the math functions,
                      # we're not 100% sure of the other digits, but
                      # we're at least not worse...
    return D(str(a)).quantize(QF) == D(str(b)).quantize(QF)
