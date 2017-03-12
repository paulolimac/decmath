# -*- coding: utf-8 -*-

"""
decmath v0.3.0
Copyright (c) 2016-2017 Evert Provoost <evert.provoost@gmail.com>

Based on dmath 0.9:
Copyright (c) 2007 Brian Beck <exogen@gmail.com>,
                   Christopher Hesse <christopher.hesse@gmail.com>


Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = "v0.3.0"

# This library aims at implementing the standard math library, (and some extras)
# starting with the most used funtions.
# If you'd have a request you can always open a ticket or even better:
# propose a pull request containing those changes.

import sys

if sys.version_info[0] != 3:
    raise ImportError("DecMath requires Python 3.")

import decimal
from decimal import Decimal, getcontext
import math as _math
from math import *

def sign(x):
    """Return -1 for negative numbers and 1 for positive numbers."""
    x = Decimal(str(x))
    return Decimal(1).copy_sign(x)

def signt(x):
    """Return -1 for negative numbers and 1 for positive numbers and 0 for zeroes and NaNs."""
    x = Decimal(str(x))
    if x == 0 or x.is_nan():
        return Decimal(0)
    else:
        return Decimal(1).copy_sign(x)

def fabs(x):
    """Return the absolute value of x."""
    return Decimal(str(x)).copy_abs()

def fsum(iterable):
    """Return an accurate floating point sum of values in the iterable."""
    sum = Decimal(0)

    for term in iterable:
        sum += Decimal(str(term))
    
    return sum

def exp(x):
    """Return e raised to the power of x.  Result type matches input type.

    >>> print(exp(Decimal(1)))
    2.718281828459045235360287471
    >>> print(exp(Decimal(2)))
    7.389056098930650227230427461
    >>> print(exp(2.0))
    7.389056098930650227230427461

    """
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

def trunc(x):
    return int(Decimal(str(x)).to_integral(rounding=decimal.ROUND_FLOOR))

def _pi():
    """Hidden function to compute Pi to the current precision."""
    getcontext().prec += 2
    lasts, t, s, n, na, d, da = 0, Decimal(3), 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

class _Constants(object):
    @property
    def pi(self):
        """Compute Pi to the current precision."""
        return _pi()
    
    @property
    def tau(self):
        """Compute Tau to the current precision."""
        return 2 * _pi()
    
    @property
    def e(self):
        """Compute the base of the natural logarithm to the current precision."""
        return exp(1)

    @property
    def phi(self):
        """Calculate the golden ratio to the current precision."""
        getcontext().prec += 2
        goldenrat = +((1 + Decimal(5).sqrt()) / 2)
        getcontext().prec -= 2
        return goldenrat
    
    @property
    def inf(self):
        """Positive infinty."""
        return  Decimal('Inf')
    
    @property
    def nan(self):
        """Not a Number."""
        return  Decimal('NaN')

    def __getattr__(self, name):
        try:
            return globals()[name]
        except KeyError:
            sys.tracebacklimit = 0
            raise AttributeError("module '" + __name__ + "' has no attribute '" + str(name) + "'")

def cos(x):
    """Return the cosine of x as measured in radians.

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.8775825618903727161162815826

    """
    x = Decimal(str(x)) % (2 * _pi())
    if isnan(x):
        return Decimal('NaN')
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

def sin(x):
    """Return the sine of x as measured in radians.

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.4794255386042030002732879352

    """
    x = Decimal(str(x)) % (2 * _pi())
    if isnan(x):
        return Decimal('NaN')
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

def cosh(x):
    """Return the hyperbolic cosine of Decimal x."""
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
    """Return the hyperbolic sine of Decimal x."""
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

# The version below is actually overwritten by the version using atan2 below
# it, since it is much faster.
def asin(x):
    """Return the arc sine (measured in radians) of Decimal x."""
    x = Decimal(str(x))

    if abs(x) > 1:
        raise ValueError("Domain error: asin accepts -1 <= x <= 1.")

    if x == -1:
        return _pi() / -2
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

# This is way faster, is there a downside?
def asin(x):
    """Return the arc sine (measured in radians) of Decimal x."""
    x = Decimal(str(x))

    if abs(x) > 1:
        raise ValueError("Domain error: asin accepts -1 <= x <= 1.")

    if x == -1:
        return _pi() / -2
    elif x == 0:
        return Decimal(0)
    elif x == 1:
        return _pi() / 2

    return atan2(x, (1 - x ** 2).sqrt())

# The version below is actually overwritten by the version using atan2 below
# it, since it is much faster.
def acos(x):
    """Return the arc cosine (measured in radians) of Decimal x."""
    x = Decimal(str(x))

    if abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1.")

    if x == -1:
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

# This is way faster, is there a downside?
def acos(x):
    """Return the arc cosine (measured in radians) of Decimal x."""
    x = Decimal(str(x))

    if abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1.")

    if x == -1:
        return _pi()
    elif x == 0:
        return _pi() / 2
    elif x == 1:
        return Decimal(0)

    return _pi() / 2 - atan2(x, Decimal(1 - x ** 2).sqrt())

def tan(x):
    """Return the tangent of Decimal x (measured in radians)."""
    return +(sin(x) / cos(x))

def tanh(x):
    """Return the hyperbolic tangent of Decimal x."""
    return +(sinh(x) / cosh(x))

def atan(x):
    """Return the arc tangent (measured in radians) of Decimal x."""
    x = Decimal(str(x))

    if x == Decimal('-Inf'):
        return _pi() / -2
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
    x_squared = x ** 2
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
    Unlike atan(y/x), the signs of both x and y are considered.
    """
    y = Decimal(str(y))
    x = Decimal(str(x))
    abs_y = abs(y)
    abs_x = abs(x)
    y_is_real = abs_y != Decimal('Inf')

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

def log(x, base=None):
    """log(x[, base]) -> the logarithm of Decimal x to the given Decimal base.
    If the base not specified, returns the natural logarithm (base e) of x.
    """
    getcontext().prec += 4

    if base == None:
        res = Decimal(str(x)).ln()

    else:
        res = Decimal(str(x)).log10() / Decimal(str(base)).log10()
    
    getcontext().prec -= 4

    return res

def log10(x):
    """log10(x) -> the base 10 logarithm of Decimal x."""
    getcontext().prec += 4
    res = Decimal(str(x)).log10()
    getcontext().prec -= 4
    return res 

def log2(x):
    """log2(x) -> the base 2 logarithm of Decimal x."""
    return log(x, 2)

def sqrt(x):
    """Return the square root of x."""
    getcontext().prec += 4
    res = Decimal(str(x)).sqrt()
    getcontext().prec -= 4
    return res

def pow(x, y):
    """Return x raised to the power y."""
    return Decimal(str(x)).__pow__(Decimal(str(y)))

def degrees(x):
    """degrees(x) -> converts Decimal angle x from radians to degrees"""
    return +(Decimal(str(x)) * (180 / _pi()))

def radians(x):
    """radians(x) -> converts Decimal angle x from degrees to radians"""
    return +(Decimal(str(x)) * (_pi() / 180))

def ceil(x):
    """Return the smallest integral value >= x."""
    return Decimal(str(x)).to_integral(rounding=decimal.ROUND_CEILING)

def floor(x):
    """Return the largest integral value <= x."""
    return Decimal(str(x)).to_integral(rounding=decimal.ROUND_FLOOR)

def hypot(x, y):
    """Return the Euclidean distance, sqrt(x*x + y*y)."""
    return sqrt(Decimal(str(x)).__pow__(2) + Decimal(str(y)).__pow__(2))

def factorial(x):
    """Return x factorial. Raises ValueError if x is not integral or is negative."""
    x = Decimal(str(x))
    x_i = int(x.to_integral_value())
    if Decimal(x_i) == x:
        if x_i >= 0:
            return _math.factorial(x_i)
        
        else:
            raise ValueError("Domain error: can't compute factorial of negative values.")
    
    else:
        raise ValueError("Domain error: can't compute factorial of non-integral values.")

def copysign(x, y):
    """Return a float with the magnitude (absolute value) of x but the sign of y.
       On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0."""
    x = Decimal(str(x))
    y = Decimal(str(y))

    return x.copy_sign(y)

def erfc(x):
    """Return the complementary error function at x."""
    # We approximate using a continued fraction which is able to give us arbitrary precision.
    x = Decimal(str(x))
    xsq = x**2

    getcontext().prec += 2

    k = getcontext().prec ** 2 # This could probably be optimised or even corrected...

    if k % 2 == 0:
        lstt = xsq
    else:
        lstt = Decimal(1)

    while k > 0:
        if k % 2 == 0:
            lstt = 1 + (k/Decimal(2)) / lstt
        else:
            lstt = xsq + (k/Decimal(2)) / lstt
        
        k -= 1

    res = (x / _pi().sqrt()) * exp(-xsq) * (1 / lstt)

    getcontext().prec -= 2

    return res

def erf(x):
    """Return the error function at x."""
    # We are able to compute erfc(x) using a continued function so...
    return 1 - erfc(x)

sys.modules[__name__] = _Constants()

__all__ = ['sign', 'signt', 'ceil', 'floor', 'factorial', 'copysign', 'fabs', 'fsum', 'trunc',
           'exp', 'log', 'log2', 'log10', 'pow', 'sqrt',
           'hypot', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2',
           'degrees', 'radians',
           'sinh', 'cosh', 'tanh',
           'erf', 'erfc',
           'pi', 'e', 'tau', 'phi', 'inf', 'nan']