from unittest.mock import Mock, patch
from app import OPS, calculate
import pytest

def test_calculate_empty_expr():
    with pytest.raises(ValueError,match="empty expression"):
        calculate("")

def test_calculate_not_str_expr():
    with pytest.raises(ValueError,match="empty expression"):
        calculate(0.0)

def test_calculate_multiple_operators():
    with pytest.raises(ValueError,match="only one operator is allowed"):
        calculate("9*9*9")

def test_calculate_invalid_format():
    with pytest.raises(ValueError,match="invalid expression format"):
        calculate("9*")
    with pytest.raises(ValueError,match="invalid expression format"):        
        calculate("/9")
    with pytest.raises(ValueError,match="invalid expression format"):
        calculate("fjosjhf20384o405r")

def test_calculate_invalid_operands():
    with pytest.raises(ValueError,match="operands must be numbers"):
        calculate("a*b")

def test_calculate_add(monkeypatch):
    mock_add = Mock(return_value=7.0)
    monkeypatch.setitem(OPS, '+', mock_add)

    result = calculate("2+5")

    assert result == 7.0
    mock_add.assert_called_once_with(2.0, 5.0)

def test_calculate_subtract(monkeypatch):
    mock_subtract = Mock(return_value=3.0)
    monkeypatch.setitem(OPS, '-', mock_subtract)

    result = calculate("6-3")

    assert result == 3.0
    mock_subtract.assert_called_once_with(6.0, 3.0)

def test_calculate_multiply(monkeypatch):
    mock_multiply = Mock(return_value=10.0)
    monkeypatch.setitem(OPS, '*', mock_multiply)

    result = calculate("2*5")

    assert result == 10.0
    mock_multiply.assert_called_once_with(2.0, 5.0)

def test_calculate_divide(monkeypatch):
    mock_divide = Mock(return_value=2.0)
    monkeypatch.setitem(OPS, '/', mock_divide)

    result = calculate("6/3")

    assert result == 2.0
    mock_divide.assert_called_once_with(6.0, 3.0)