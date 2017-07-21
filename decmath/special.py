from decimal import getcontext, Decimal
from decmath import exp, ceil

## Special functions

def erf(x):
    """Return the error function at x."""
    if x >= getcontext().prec / 10 + 6:
        return Decimal(1) # This isn't worth the computation time.
    else:
        # We are able to compute erfc(x) using a continued fraction so...
        return 1 - erfc(x)

def erfc(x):
    """Return the complementary error function at x."""
    # We approximate using a continued fraction which is able to give us
    # arbitrary precision.
    x = Decimal(str(x)) 

    getcontext().prec += int(ceil(x)) ** 2 + 2
    k = getcontext().prec ** 2 # This could probably be optimised or even
                               # corrected...

    lstt = x

    while k > 0:
        lstt = 2*x + Decimal(2 * k) / lstt
        k -= 1

    res = 2 * exp(-x ** 2) / (_pi()).sqrt() * (1 / lstt)
    getcontext().prec -= int(ceil(x)) ** 2 + 2
    return +res
