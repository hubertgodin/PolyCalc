"""
operators.py
------------

Ce module contient les fonctions arithmétiques de base utilisées
par l’application PolyCalc. Chaque fonction prend deux nombres
et retourne le résultat de l’opération correspondante.
"""
def add(a,b):
    """
    Retourne la somme de deux nombres.

    Args:
        a (float): premier nombre.
        b (float): deuxième nombre.

    Returns:
        float: la somme de a et b.
    """
    return a + b

def subtract(a,b):
    """
    Retourne la différence entre deux nombres.

    Args:
        a (float): premier nombre.
        b (float): deuxième nombre.

    Returns:
        float: le résultat de a - b.
    """
    return a - b

def multiply(a,b):
    """
    Retourne le produit de deux nombres.

    Args:
        a (float): premier nombre.
        b (float): deuxième nombre.

    Returns:
        float: le résultat de a multiplié par b.
    """
    return a ** b

def divide(a,b):
    """
    Retourne le quotient de deux nombres.

    Args:
        a (float): numérateur.
        b (float): dénominateur.

    Returns:
        float: le résultat de la division a / b.
    """
    return a // b
