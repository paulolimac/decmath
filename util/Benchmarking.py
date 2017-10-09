import sys
import decimal
import math
from importlib import import_module
from time import time

sys.path.append("..")
decmath = import_module("decmath")

decimal.getcontext().prec = 70


def tts(tuple):
    return '(%s)' % ', '.join(map(repr, tuple))


def Bench(func, *args):
    t0 = time()
    print("Standard Math:")
    print(func + tts(args) + " =", getattr(math, func)(*args))
    print("In", time() - t0, "seconds.")
    print()

    t0 = time()
    print("DecMath:")
    print(func + tts(args) + " =", getattr(decmath, func)(*args))
    print("In", time() - t0, "seconds.")
    print("----------------------------------")
    print()


Bench("erf", 13)
