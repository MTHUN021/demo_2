from assign_4 import *
from assign_5 import *

import pytest

@pytest.fixture
def get_c1():
    return complex_no(2,2)


@pytest.fixture
def get_c2():
    return complex_no(1,3)


@pytest.fixture
def get_b1():
    return Bank_account("50387823", 10000, 100)


@pytest.fixture
def get_p1():
    return Point(2, 9)


@pytest.fixture
def get_p2():
    return Point(4, 6)


@pytest.fixture
def get_co1():
    return color((255, 0, 255))


@pytest.fixture
def get_co2():
    return color((0, 0, 255))


@pytest.fixture
def get_ci1():
    return circle(5)



@pytest.fixture
def get_r1():
    return rectangle(4, 3)


@pytest.fixture
def get_bo1():
    return box(2, 4, 6)


@pytest.fixture
def get_i1():
    return ipaddress(382156382)


@pytest.fixture
def get_ti1():
    return time(11, 23, 22)


@pytest.fixture
def get_ti2():
    return time(29, 99, 90)


@pytest.fixture
def get_st1():
    return Stack(10, [1, 2, 3])


@pytest.fixture
def get_di1():
    return Distance(12, 13)


@pytest.fixture
def get_di2():
    return Distance(5, 3)


@pytest.fixture
def get_ba1():
    return Bank_account_with_exp("8162319", 100000, 8000)


@pytest.fixture
def m1():
    return mobile_billing_with_exp(2000, 100, "POSTPAID", 1000, "NO")



def test_func(get_c1, get_c2):
    res = get_c1 + get_c2
    
    assert complex_no(3, 5) == res
    pass





