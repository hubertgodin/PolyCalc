"""
test_app.py
------------

Ce module contient les tests pour l’application web Flask PolyCalc.

Les tests utilisent le client de test de Flask pour simuler des requêtes HTTP
et vérifier que :
- La page principale ('/') s’affiche correctement.
- Les éléments de l’interface (titre, boutons, champ d’affichage) sont présents.
- Le fichier CSS statique est accessible et contient les styles attendus.

BeautifulSoup est utilisé pour analyser le HTML et vérifier la présence des éléments.
"""

import pytest
from app import app
from bs4 import BeautifulSoup
from pytest_check import check

@pytest.fixture
def client():
    """
    Fixture Pytest qui crée un client de test pour l’application Flask.

    Cette fixture permet d’envoyer des requêtes HTTP simulées à l’application
    sans lancer le serveur réel.

    Yields:
        client (FlaskClient): instance du client de test configurée en mode test.
    """
    app.config["TESTING"]=True
    with app.test_client() as client:
        yield client

def test_get(client):
    """
    Teste la requête GET vers la page d’accueil ('/').

    Vérifie que :
        - Le code de statut HTTP est 200 (succès)
        - Le titre <h1>PolyCalc</h1> est présent dans la page
        - L’élément d’affichage (id='display') existe et est vide au départ
        - Tous les boutons de la calculatrice (0–9, +, -, *, /, =, C) sont présents

    Utilise BeautifulSoup pour analyser le contenu HTML.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>PolyCalc</h1>' in response.data

    soup = BeautifulSoup(response.data.decode('utf-8'),'html.parser')
    display_element = soup.find(id="display")
    assert display_element.get('value') == ""

    actual_labels = [btn.text for btn in soup.find_all("button",class_="btn")]

    expected_labels = [str(i) for i in range(10)] + ['+','-','x','÷','=','C']
    for expected in expected_labels:
        check.is_in(expected,actual_labels,"Button label " + expected + " is missing from HTML file")

def test_get_style(client):
    """
    Teste l’accès au fichier CSS statique (style.css).

    Vérifie que :
        - Le fichier est bien accessible (code 200)
        - Il contient la règle 'body {' indiquant le début des styles de la page
    """
    response = client.get('/static/style.css')
    assert response.status_code == 200
    assert b'body {' in response.data
        
def test_post(client,mocker):
    payload = {
    'display': '4+6',
    }
    mocker.patch('app.calculate', return_value=10.0)
    response =  client.post('/',data=payload)
    assert response.status_code == 200
    soup = BeautifulSoup(response.data.decode('utf-8'),'html.parser')
    display_element = soup.find(id="display")
    assert "10.0" == display_element.get('value')

def test_not_found(client):
    response = client.get('/invalid')
    assert response.status_code == 404