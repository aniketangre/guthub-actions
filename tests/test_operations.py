from src.math_operations import add, subtract

def test_add():
    assert add(2,3)==5
    assert add(4,-1)==3
    assert add(-1,1)==0

def test_subtract():
    assert subtract(2,3)==-1
    assert subtract(4,-1)==5
    assert subtract(-1,1)==-2

