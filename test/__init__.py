import sys 
sys.path.append('..')

import decmath as dm
import math as m
from decimal import Decimal as D

def abteq(a, b):
    QF = D(10) ** -15 # This is the precission of the math functions,
                      # we're not 100% sure of the other digits, but
                      # we're at least not worse...
    return D(a).quantize(QF) == D(b).quantize(QF)
