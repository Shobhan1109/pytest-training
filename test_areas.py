import ares

def test_recA():
    x=10
    y=30
    r=ares.recA(x, y)
    assert x*y == r

def test_recP():
    x=10
    y=30
    r=ares.recP(x,y)
    assert 2*(x+y) == r

def test_square():
    x=10
    r=ares.square(x)
    assert x*x == r