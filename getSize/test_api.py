from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_add_item():
    response = client.get(
        "/size",
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Total objects 0",
    }
