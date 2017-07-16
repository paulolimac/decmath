# -*- coding: utf-8 -*-

"""
decmath v0.3.1
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

# This document contains some alternative algorithms which are usualy slower,
# however they might be better...

def asin(x):
    """Return the arc sine (measured in radians) of x."""
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

def acos(x):
    """Return the arc cosine (measured in radians) of x."""
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
