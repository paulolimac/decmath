from decimal import Decimal
from decmath import _pi

## Angular conversion

def degrees(x):
    """degrees(x) -> converts angle x from radians to degrees"""
    return Decimal(str(x)) * 180 / _pi()

def radians(x):
    """radians(x) -> converts angle x from degrees to radians"""
    return Decimal(str(x)) * _pi() / 180
