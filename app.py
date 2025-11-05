"""
app.py
-------

Ce module est le cœur de l’application Flask PolyCalc.
Il définit les routes de l’application et relie le frontend (HTML)
au backend (fonctions mathématiques définies dans operators.py).

Fonctionnalités :
- Affiche une interface web simple permettant d’entrer une expression arithmétique.
- Analyse et évalue l’expression saisie (ex : 2+3 ou 10/5).
- Gère les erreurs de saisie (opérateurs multiples, valeurs invalides, etc.).
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Initialisation de l'application Flask
app = Flask(__name__)

# Dictionnaire associant chaque opérateur à la fonction correspondante
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse et évalue une expression mathématique simple contenant deux opérandes
    et un opérateur (ex. "2+3", "5 / 2").

    Args:
        expr (str): L’expression arithmétique à évaluer. Exemple : "4*2".

    Returns:
        float: Le résultat de l’opération.

    Raises:
        ValueError: Si l’expression est vide, mal formée, ou contient plusieurs opérateurs.
        ValueError: Si les opérandes ne sont pas des nombres valides.
        ValueError: Si la division par zéro est tentée.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")
    # On enlève les espaces pour simplifier le traitement
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None
    # On cherche l'opérateur dans la chaîne
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Plus d’un opérateur trouvé → erreur
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch
    # Vérifie que l'opérateur n'est ni au début ni à la fin
    if op_pos <= 0 or op_pos >= len(s) - 1:

        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")
    # On appelle la bonne fonction à partir du dictionnaire OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
       Route principale de l’application.

       - En GET : affiche la page de la calculatrice.
       - En POST : récupère l’expression envoyée par le formulaire HTML,
         tente de la calculer et affiche le résultat.

       Retour :
           str : Le HTML rendu pour la page index.html avec le résultat intégré.
       """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Mode debug activé pour faciliter le développement
    app.run(debug=True)