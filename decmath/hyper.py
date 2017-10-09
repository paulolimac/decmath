from decimal import getcontext, Decimal
from decmath import sign

# Hyperbolic functions


def acosh(x):
    """Return the inverse hyperbolic cosine of x."""
    x = Decimal(str(x))

    if abs(x) < 1:
        raise ValueError("Domain error: acosh accepts x > 1.")

    elif abs(x) == 1:
        return Decimal('0')

    else:
        return (x + (x**2 - 1).sqrt()).ln()


def asinh(x):
    """Return the inverse hyperbolic sine of x."""
    x = Decimal(str(x))
    return (x + (1 + x**2).sqrt()).ln()


def atanh(x):
    """Return the inverse hyperbolic tangent of x."""
    x = Decimal(str(x))

    if abs(x) > 1:
        raise ValueError("Domain error: atanh accepts -1 <= x <= 1.")

    elif abs(x) == 1:
        return sign(x) * Decimal('Inf')

    else:
        return Decimal('0.5') * ((1 + x) / (1 - x)).ln()


def cosh(x):
    """Return the hyperbolic cosine of x."""
    x = Decimal(str(x))

    if x == 0:
        return Decimal(1)

    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        num *= x * x
        fact *= i * (i - 1)
        s += num / fact
    getcontext().prec -= 2
    return +s


def sinh(x):
    """Return the hyperbolic sine of x."""
    x = Decimal(str(x))

    if x == 0:
        return Decimal(0)

    getcontext().prec += 2
    i, lasts, s, fact, num = 1, 0, x, 1, x
    while s != lasts:
        lasts = s
        i += 2
        num *= x * x
        fact *= i * (i - 1)
        s += num / fact
    getcontext().prec -= 2
    return +s


def tanh(x):
    """Return the hyperbolic tangent of x."""
    return +(sinh(x) / cosh(x))
