from decimal import getcontext, Decimal
from decmath import _pi, sign

# Trigonometric functions


def acos(x):
    """Return the arc cosine (measured in radians) of x."""
    x = Decimal(str(x))

    if x.is_nan():
        return Decimal("NaN")
    elif abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1.")
    elif x == -1:
        return _pi()
    elif x == 0:
        return _pi() / 2
    elif x == 1:
        return Decimal(0)

    getcontext().prec += 2
    one_half = Decimal('0.5')
    i, lasts, s, gamma, fact, num = Decimal(0), 0, _pi() / 2 - x, 1, 1, x
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x * x
        gamma *= i - one_half
        coeff = gamma / ((2 * i + 1) * fact)
        s -= coeff * num
    getcontext().prec -= 2
    return +s


def asin(x):
    """Return the arc sine (measured in radians) of x."""
    x = Decimal(str(x))

    if x.is_nan():
        return Decimal("NaN")
    elif abs(x) > 1:
        raise ValueError("Domain error: asin accepts -1 <= x <= 1.")
    elif x == -1:
        return -_pi() / 2
    elif x == 0:
        return Decimal(0)
    elif x == 1:
        return _pi() / 2

    getcontext().prec += 2
    one_half = Decimal('0.5')
    i, lasts, s, gamma, fact, num = Decimal(0), 0, x, 1, 1, x
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x * x
        gamma *= i - one_half
        coeff = gamma / ((2 * i + 1) * fact)
        s += coeff * num
    getcontext().prec -= 2
    return +s


def atan(x):
    """Return the arc tangent (measured in radians) of x."""
    x = Decimal(str(x))

    if x.is_nan():
        return Decimal("NaN")
    elif x == Decimal('-Inf'):
        return -_pi() / 2
    elif x == 0:
        return Decimal(0)
    elif x == Decimal('Inf'):
        return _pi() / 2

    if x < -1:
        c = _pi() / -2
        x = 1 / x
    elif x > 1:
        c = _pi() / 2
        x = 1 / x
    else:
        c = 0

    getcontext().prec += 2
    x_squared = x**2
    y = x_squared / (1 + x_squared)
    y_over_x = y / x
    i, lasts, s, coeff, num = Decimal(0), 0, y_over_x, 1, y_over_x
    while s != lasts:
        lasts = s
        i += 2
        coeff *= i / (i + 1)
        num *= y
        s += coeff * num
    if c:
        s = c - s
    getcontext().prec -= 2
    return +s


def atan2(y, x):
    """Return the arc tangent (measured in radians) of y/x.
    Unlike atan(y/x), the signs of both x and y are considered."""
    y = Decimal(str(y))
    x = Decimal(str(x))
    abs_y = abs(y)
    abs_x = abs(x)
    y_is_real = abs_y != Decimal('Inf')

    if y.is_nan() or x.is_nan():
        return Decimal("NaN")

    if x:
        if y_is_real:
            a = y and atan(y / x) or Decimal(0)
            if x < 0:
                a += sign(y) * _pi()
            return a
        elif abs_y == abs_x:
            x = sign(x)
            y = sign(y)
            return _pi() * (Decimal(2) * abs(x) - x) / (Decimal(4) * y)
    if y:
        return atan(sign(y) * Decimal('Inf'))
    elif sign(x) < 0:
        return sign(y) * _pi()
    else:
        return sign(y) * Decimal(0)


def cos(x):
    """Return the cosine of x as measured in radians."""
    x = Decimal(str(x)) % (2 * _pi())

    if x.is_nan():
        return Decimal('NaN')
    elif x == _pi() / 2 or x == 3 * _pi() / 2:
        return Decimal(0)

    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def hypot(x, y):
    """Return the Euclidean distance, sqrt(x*x + y*y)."""
    return (Decimal(str(x)).__pow__(2) + Decimal(str(y)).__pow__(2)).sqrt()


def sin(x):
    """Return the sine of x as measured in radians."""
    x = Decimal(str(x)) % (2 * _pi())

    if x.is_nan():
        return Decimal('NaN')
    elif x == 0 or x == _pi():
        return Decimal(0)

    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def tan(x):
    """Return the tangent of x (measured in radians)."""
    x = Decimal(str(x))

    if x.is_nan():
        return Decimal('NaN')
    elif x == _pi() / 2:
        return Decimal('Inf')
    elif x == 3 * _pi() / 2:
        return Decimal('-Inf')
    return sin(x) / cos(x)
