import calculator

def test_add():
    x=10
    y=20
    r=calculator.add(x, y)
    assert x+y == r

def test_sub():
    x=10
    y=20
    r=calculator.sub(x, y)
    assert x-y == r

def test_mult():
    x=10
    y=20
    r=calculator.mult(x, y)
    assert x*y == r

def test_div():
    x=10
    y=20
    r=calculator.div(x, y)
    assert x/y == r