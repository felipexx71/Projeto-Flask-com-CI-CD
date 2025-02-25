import pytest
from app import app 

@pytest.fixture
def client():
    return app.test_client() 

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "API funcionando!"}

def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
