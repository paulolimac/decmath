from decimal import Decimal as D
from decimal import getcontext

import sys
sys.path.append("..")


def abteq(a, b):
    """About equal, to compare DecMath and math"""
    QF = D(10)**-12  # This is the precission of the math functions,
    # we're not 100% sure of the other digits, but
    # we're at least not worse...
    return D(str(a)).quantize(QF) == D(str(b)).quantize(QF)


def msteq(a, b):
    """(Al)most equal, to negate very small errors in DecMath"""
    expon = D(getcontext().prec) - 3
    QF = D(10)**-expon
    return D(str(a)).quantize(QF) == D(str(b)).quantize(QF)
