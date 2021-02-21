from assign_4 import *
from assign_5 import *

import pytest

@pytest.fixture
def get_c1():
    return complex_no(2,2)


@pytest.fixture
def get_c2():
    return complex_no(1,3)


def test_func(get_c1, get_c2):
    res = get_c1 + get_c2
    
    assert complex_no(3, 5) == res
    pass



