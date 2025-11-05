import pytest
from app import app
from bs4 import BeautifulSoup

@pytest.fixture
def client():
    app.config["TESTING"]=True
    with app.test_client() as client:
        yield client

def test_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>PolyCalc</h1>' in response.data
    
    soup = BeautifulSoup(response.data.decode('utf-8'),'html.parser')
    display_element = soup.find(id="display")
    assert display_element.text == ""

    btns = soup.find_all("button",class_="btn")

    labels = [str(i) for i in range(10)] + ['+','-','*','/','=','C']
    for btn in btns:
        assert btn.text in labels

def test_get_style(client):
    response = client.get('/static/style.css')
    assert b'body {' in response.data
        

