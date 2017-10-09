from decimal import getcontext, Decimal

# Power and logarithmic functions


def exp(x):
    """Return e raised to the power of x."""
    x = Decimal(str(x))
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s


def expm1(x):
    """Return e raised to the power of x, minus one."""
    # Decimal handles this perfecly so no need for complexity
    return exp(x) - 1


def log(x, base=None):
    """log(x[, base]) -> the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x."""
    if base is None:
        res = Decimal(str(x)).ln()

    elif base == 10:
        res = Decimal(str(x)).log10()

    else:
        res = Decimal(str(x)).log10() / Decimal(str(base)).log10()

    return +res


def log1p(x):
    """Return the natural logarithm of 1+x (base e)."""
    # Decimal handles this perfecly so no need for complexity.
    return (1 + Decimal(str(x))).ln()


def log2(x):
    """log2(x) -> the base 2 logarithm of x."""
    return Decimal(str(x)).log10() / Decimal(2).log10()


def log10(x):
    """log10(x) -> the base 10 logarithm of x."""
    return Decimal(str(x)).log10()


def pow(x, y):
    """Return x raised to the power y."""
    return Decimal(str(x)).__pow__(Decimal(str(y)))


def sqrt(x):
    """Return the square root of x."""
    return Decimal(str(x)).sqrt()
