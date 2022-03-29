import calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(3,2,5),(4,2,6),(5,5,10),(5,5,9)])
def test_add(a,b,c):
    r=calculator.add(a,b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,1),(4,2,2),(5,5,0),(5,5,9)])
def test_sub(a,b,c):
    r=calculator.sub(a, b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,6),(4,2,8),(5,5,25),(5,5,9)])
def test_mult(a,b,c):
    r=calculator.mult(a, b)
    assert r == c

@pytest.mark.parametrize("a,b,c",[(3,2,1.5),(4,2,2),(5,5,1),(5,5,9)])
def test_div(a,b,c):
    r=calculator.div(a, b)
    assert r == c