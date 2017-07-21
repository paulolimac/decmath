from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
import math

## Number-theoretic and representation functions

def ceil(x):
    """Return the smallest integral value >= x."""
    return Decimal(str(x)).to_integral(rounding=ROUND_CEILING)

def copysign(x, y):
    """Return a float with the magnitude (absolute value) of x but the sign of
       y. On platforms that support signed zeros, copysign(1.0, -0.0)
       returns -1.0."""
    x = Decimal(str(x))
    y = Decimal(str(y))

    return x.copy_sign(y)

def fabs(x):
    """Return the absolute value of x."""
    return Decimal(str(x)).copy_abs()

def factorial(x):
    """Return x factorial. Raises ValueError if x is not integral or is
       negative."""
    x = Decimal(str(x))
    x_i = int(x.to_integral_value())
    if Decimal(x_i) == x:
        if x_i >= 0:
            return math.factorial(x_i)
        
        else:
            raise ValueError(
                "Domain error: can't compute factorial of negative values.")
    
    else:
        raise ValueError(
            "Domain error: can't compute factorial of non-integral values.")

def floor(x):
    """Return the largest integral value <= x."""
    return Decimal(str(x)).to_integral(rounding=ROUND_FLOOR)

def fmod(x, y):
    """Returns the remainder of x and y, using the remainder_near() function
       in Decimal, which comes close to the function in the math library"""
    return Decimal(str(x)).remainder_near(Decimal(str(y)))

def frexp(x):
    """Return the mantissa and exponent of x as the pair (m, e). m is a Decimal
       and e is an integer such that x == m * 2**e exactly. If x is zero,
       returns (0.0, 0), otherwise 0.5 <= abs(m) < 1."""
    e = math.frexp(x)[1]
    x = Decimal(str(x))
    return (x / (Decimal(2**e)), e)

def fsum(iterable):
    """Return an accurate floating point sum of values in the iterable."""
    sum = Decimal(0)

    for term in iterable:
        sum += Decimal(str(term))
    
    return sum

def isclose(a, b, *, rel_tol=Decimal(10)**-9, abs_tol=Decimal('0.0')):
    """Return True if the values a and b are close to each other and False
       otherwise. Whether or not two values are considered close is determined
       according to given absolute and relative tolerances.

       rel_tol is the relative tolerance –- it is the maximum allowed difference
       between a and b, relative to the larger absolute value of a or b.
       For example, to set a tolerance of 5%, pass rel_tol=0.05. The default
       tolerance is 1e-09, which assures that the two values are the same within
       about 9 decimal digits. rel_tol must be greater than zero.

       abs_tol is the minimum absolute tolerance -– useful for comparisons near
       zero. abs_tol must be at least zero.

       If no errors occur, the result will be:
       abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

       The IEEE 754 special values of NaN, inf, and -inf will be handled
       according to IEEE rules. Specifically, NaN is not considered close to any
       other value, including NaN. inf and -inf are only considered close to
       themselves."""
    a = Decimal(str(a))
    b = Decimal(str(b))
    if a.is_nan() or b.is_nan():
        return False
    elif a.is_infinite() and b.is_infinite():
        if sign(a) == sign(b):
            return True
        else:
            return False
    elif a.is_infinite() or b.is_infinite():
        return False
    else:
        return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def ldexp(x, i):
    """Return x * (2**i). This is essentially the inverse of function
       frexp()."""
    return Decimal(str(x)) * (2**Decimal(str(i)))

def modf(x):
    """Return the fractional and integer parts of x. Both results carry
       the sign of x."""
    x = Decimal(str(x))
    return (sign(x) * (abs(x) - floor(abs(x))), sign(x) * floor(abs(x)))

def remainder(x, y):
    """Returns the remainder of x and y, using the remainder_near() function
       in Decimal, which comes close to the function in the math library"""
    return Decimal(str(x)).remainder_near(Decimal(str(y)))

def sign(x): 
    """Return -1 for negative numbers and 1 for positive numbers."""
    x = Decimal(str(x))
    return Decimal(1).copy_sign(x)

def signt(x):
    """Return -1 for negative numbers and 1 for positive numbers and 0 for
       zeroes and NaNs."""
    x = Decimal(str(x))
    if x == 0 or x.is_nan():
        return Decimal(0)
    else:
        return Decimal(1).copy_sign(x)
