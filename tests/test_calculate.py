"""
test_calculate.py
-----------------
Ce module contient les tests unitaires de la fonction `calculate()` définie dans `app.py`.
Les tests vérifient :
- la gestion des entrées invalides,
- la validation des formats d’expression,
- et le bon appel des fonctions arithmétiques du dictionnaire `OPS`.

Chaque test utilise le framework `pytest` pour vérifier que les erreurs sont levées correctement
et que les opérations valides produisent les bons résultats.
"""


from unittest.mock import Mock, patch
from app import OPS, calculate
import pytest

def test_calculate_empty_expr():
    """Vérifie que `calculate()` lève une ValueError si l’expression est vide."""
    with pytest.raises(ValueError,match="empty expression"):
        calculate("")

def test_calculate_not_str_expr():
    """Vérifie que `calculate()` lève une ValueError si l’entrée n’est pas une chaîne de caractères."""
    with pytest.raises(ValueError,match="empty expression"):
        calculate(0.0)

def test_calculate_multiple_operators():
    """Teste qu’une expression contenant plusieurs opérateurs simultanés est rejetée."""
    with pytest.raises(ValueError,match="only one operator is allowed"):
        calculate("9*9*9")

def test_calculate_invalid_format():
    """
    Vérifie que `calculate()` lève une erreur pour les expressions mal formées.
    Cas testés :
    - opérateur sans second opérande
    - opérateur en début d’expression
    - chaîne contenant des caractères non numériques
    """
    with pytest.raises(ValueError,match="invalid expression format"):
        calculate("9*")
    with pytest.raises(ValueError,match="invalid expression format"):        
        calculate("/9")
    with pytest.raises(ValueError,match="invalid expression format"):
        calculate("fjosjhf20384o405r")

def test_calculate_invalid_operands():
    """Teste que `calculate()` rejette les expressions avec des opérandes non numériques."""
    with pytest.raises(ValueError,match="operands must be numbers"):
        calculate("a*b")

def test_calculate_add(monkeypatch):
    """Vérifie que `calculate()` appelle correctement la fonction d’addition (`+`)."""
    # On remplace temporairement la fonction '+' par un mock
    mock_add = Mock(return_value=7.0)
    monkeypatch.setitem(OPS, '+', mock_add)

    result = calculate("2+5")
    # Vérifications

    assert result == 7.0
    mock_add.assert_called_once_with(2.0, 5.0)

def test_calculate_subtract(monkeypatch):
    """Vérifie que `calculate()` appelle correctement la fonction de soustraction (`-`)."""
    mock_subtract = Mock(return_value=3.0)
    monkeypatch.setitem(OPS, '-', mock_subtract)

    result = calculate("6-3")
    # Vérifications
    assert result == 3.0
    mock_subtract.assert_called_once_with(6.0, 3.0)

def test_calculate_multiply(monkeypatch):
    """Vérifie que `calculate()` appelle correctement la fonction de multiplication (`*`)."""
    mock_multiply = Mock(return_value=10.0)
    monkeypatch.setitem(OPS, '*', mock_multiply)

    result = calculate("2*5")

    assert result == 10.0
    mock_multiply.assert_called_once_with(2.0, 5.0)

def test_calculate_divide(monkeypatch):
    """Vérifie que `calculate()` appelle correctement la fonction de division (`/`)."""
    mock_divide = Mock(return_value=2.0)
    monkeypatch.setitem(OPS, '/', mock_divide)

    result = calculate("6/3")

    assert result == 2.0
    mock_divide.assert_called_once_with(6.0, 3.0)