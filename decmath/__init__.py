"""
decmath v0.4.0
Copyright (c) 2016-present Evert Provoost <evert.provoost@gmail.com>

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

__version__ = "0.4.0"

# This library aims at implementing the standard math library, (and some extras)
# starting with the most used funtions.
# If you'd have a request you can always open a ticket or even better:
# propose a pull request containing those changes.

import sys
import math
from decimal import getcontext, Decimal

if sys.version_info.major != 3:
    raise ImportError("DecMath requires Python 3.")

# This constant has to be available to the other parts of DecMath.
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

# Import the subfiles into the decmath namespace.
from decmath.num_repr import *
from decmath.pow_log import *
from decmath.trig import *
from decmath.ang_conv import *
from decmath.hyper import *
from decmath.special import *

# Now add the constants using some neat/hacky code...
class _Constants:

    @property
    def phi(self):
        """Calculate the golden ratio to the current precision."""
        return (1 + Decimal(5).sqrt()) / 2

    @property
    def pi(self):
        """Compute Pi to the current precision."""
        return _pi()

    @property
    def e(self):
        """Compute the base of the natural logarithm to the current
           precision."""
        getcontext().prec += 2
        i, lasts, s, fact = 0, 0, 1, Decimal(1)
        while s != lasts:
            lasts = s
            i += 1
            fact *= i
            s += 1 / fact
        getcontext().prec -= 2
        return +s

    @property
    def tau(self):
        """Compute Tau to the current precision."""
        return 2 * _pi()

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
            sys.tracebacklimit = 1
            raise AttributeError("module '" + __name__ + "' has no attribute '"
                + str(name) + "'")

sys.modules[__name__] = _Constants()

__all__ = ['ceil', 'copysign', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
               'fsum', 'isclose', 'ldexp', 'modf', 'remainder', 'sign', 'signt',
           'exp', 'expm1', 'log', 'log1p', 'log2', 'log10', 'pow', 'sqrt',
           'acos', 'asin', 'atan', 'atan2', 'cos', 'hypot', 'sin', 'tan',
           'degrees', 'radians',
           'acosh', 'asinh', 'atanh', 'cosh', 'sinh', 'tanh',
           'erf', 'erfc',
           'phi', 'pi', 'e', 'tau', 'inf', 'nan']

__delibnotimpltd__ = ['gamma', 'lgamma',
                      'gcd', 'isnan', 'isinf', 'isfinite', 'trunc']

# Now add any missing functions.
for funct in dir(math):
    if not funct in globals().keys():
        globals()[funct] = getattr(math, funct)
