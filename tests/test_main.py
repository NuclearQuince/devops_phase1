# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'


def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_get_item():
    response = client.get('/items/42')
    assert response.status_code == 200
    assert response.json() == {'item_id': 42, 'name': 'Item 42'}
