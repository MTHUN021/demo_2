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
    return time(9, 99, 90)


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
    return Bank_account("8162319", 100000, 5000)


@pytest.fixture
def m1():
    return mobile_billing(2000, 100, "POSTPAID", 1000, "NO")



def test_func(get_c1, get_c2):
    '''Complex nos'''


    res = get_c1 + get_c2
    res1 = get_c1 - get_c2
    
    assert complex_no(3, 5) == res
    assert complex_no(1, -1) == res1
    assert (get_c2 == get_c1) == False


def test_func2(get_di1, get_di2):
    '''Distance Class'''


    res = get_di1 + get_di2
    
    assert Distance(18, 4) == res
    assert (get_di2 == get_di1) == False
    assert get_di1.inches == 1


def test_func3(get_ti1, get_ti2):
    '''Time class'''

    res = get_ti1 + get_ti2

    assert time(23, 3, 52) == res
    assert get_ti2.min == 40
    assert get_ti2.sec == 30
    assert (get_ti2 == get_ti1) == False


def test_func4(get_p1, get_p2):
    ''' Point class'''


    assert (get_p2 == get_p1) == False
    assert get_p1.x == 2
    assert get_p2.quad() == 1


def test_func5(get_ba1):
    '''Bank account'''

    assert get_ba1.balance == 100000
    assert get_ba1.debit(2000) == 98000
    assert get_ba1.credit(5000) == 103000

def test_func6(get_co1):
    '''Color class'''

    assert get_co1.red == 255
    assert get_co1.form_color() == 'magenta'


def test_func7(get_st1):
    '''Stack Class'''

    assert get_st1.elements == [1, 2, 3]
    assert get_st1.pop_ele() == 3
    get_st1.push_ele(9)
    assert get_st1.elements == [1, 2, 9]