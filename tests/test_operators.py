"""
test_operators.py
-----------------

Ce module contient les tests unitaires pour les fonctions du module operators.py.
Il permet de vérifier que chaque opération (add, subtract, multiply, divide)
retourne le résultat attendu.
"""
from operators import add, divide,multiply,subtract
import pytest

def test_add():
    """Teste que add() retourne la somme correcte."""
    assert add(2,3) == 5
    assert add(1000,8000) == 9000
    assert add(-1,1) ==0
    assert add(-5, -7) == -12
    assert add(0,0) == 0
    assert add(5,-10) == -5
    assert add(2.5,6) == 8.5
    assert add(0.1, 0.9) ==1

def test_subtract():
    """Teste que subtract() retourne la différence correcte."""
    assert subtract(1,9) ==-8
    assert subtract(1,1) == 0
    assert subtract(8, 11) == -3
    assert subtract(-9,7) ==-16
    assert subtract(10, -15) ==25
    assert subtract(2.5,0.5) ==2
    assert subtract(1, 0.4) ==0.6
    assert subtract(3, 0) ==3

def test_multiply():
    """Teste que multiply() retourne le produit correct."""
    assert multiply(10,5) ==50
    assert multiply(-4,5) == -20
    assert multiply(2.5, 4) ==10
    assert multiply(5.5,6.5) ==35.75
    assert multiply(-6,-7) == 42
    assert multiply(1,2) ==2
    assert multiply(99,0) ==0

def test_divide():
    """Teste que divide() retourne le quotient correct"""
    assert divide(10,5) ==2
    assert divide(10,4) == 2.5
    assert divide(100,-1) ==-100
    assert divide(-50,-10) ==5
    assert divide(0,4) == 0
    assert divide(8,0.4) == 20
    assert divide(0.2, 2) ==0.1

def test_divide_by_zero():
      "Teste que divide() gère la division par zéro"
      with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(99,0)

