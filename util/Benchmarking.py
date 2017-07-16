import sys 
sys.path.append('..')

import math
import decmath
from time import time

import decimal
decimal.getcontext().prec = 70

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

Bench("erf", 13)

# 70 -> 13
# 60 -> 12
# 50 -> 11
# 40 -> 10
# 30 -> 9
# 20 -> 7
# 10 -> 5