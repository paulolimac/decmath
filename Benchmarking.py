#!/usr/bin/env python3

import math
import decmath
from time import time

def tts(tuple):
    return '(%s)' % ', '.join(map(repr, tuple))

def Bench(func, *args):
    t0 = time()
    print("Standard Math:")
    print(func + tts(args) + " =", eval("math." + func + str(args)))
    print("In", time() - t0, "seconds.")
    print()

    t0 = time()
    print("DecMath:")
    print(func + tts(args) + " =", eval("decmath." + func + str(args)))
    print("In", time() - t0, "seconds.")
    print("----------------------------------")
    print()

Bench("exp", 10)