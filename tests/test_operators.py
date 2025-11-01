from operators import add, divide,multiply,subtract
import pytest

def test_add():
    assert add(2,3) == 5
    assert add(1000,8000) == 9000
    assert add(-1,1) ==0
    assert add(-5, -7) == -12
    assert add(0,0) == 0
    assert add(5,-10) == -5
    assert add(2.5,6) == 8.5
    assert add(0.1, 0.9) ==1

def test_subtract():
    assert subtract(1,9) ==-8
    assert subtract(1,1) == 0
    assert subtract(8, 11) == -3
    assert subtract(-9,7) ==-16
    assert subtract(10, -15) ==25
    assert subtract(2.5,0.5) ==2
    assert subtract(1, 0.4) ==0.6
    assert subtract(3, 0) ==3

def test_multiply():
    assert multiply(10,5) ==50
    assert multiply(-4,5) == -20
    assert multiply(2.5, 4) ==10
    assert multiply(5.5,6.5) ==35.75
    assert multiply(-6,-7) == 42
    assert multiply(1,2) ==2
    assert multiply(99,0) ==0

def test_divide():
    assert divide(10,5) ==2
    assert divide(10,4) == 2.5
    assert divide(100,-1) ==-100
    assert divide(-50,-10) ==5
    assert divide(0,4) == 0
    assert divide(8,0.4) == 20
    assert divide(0.2, 2) ==0.1
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(99,0)

