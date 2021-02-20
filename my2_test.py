from assign_4 import *
from assign_5 import *

import pytest

@pytest.fixture
def get_c1():
    return complex(2,2)

@pytest.fixture
def get_c2():
    return complex(1,3)

def test_add(get_c1, get_c2):
    res = get_c1 + get_c2
    res1 = get_c1 * get_c2
    assert str(res) == "3 + 5j"
    assert str(res1) == "-4 + 8j"
