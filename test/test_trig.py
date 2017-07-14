import sys 
sys.path.append('..')

import decmath as dm

def test_cos():
    assert dm.cos(0) == 1
