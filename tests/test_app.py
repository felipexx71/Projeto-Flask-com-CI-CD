import pytest
from app import app 

@pytest.fixture
def client():
    return app.test_client() 

def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
