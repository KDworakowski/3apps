from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_add_item():
    response = client.post(
        "/add",
        json={"taskid": "task1234", "description": "Example description", "params": {"test1": "1234","test2": "5678"}}
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Task task1234 added",
    }

def test_add_item_bad_request():
    response = client.post(
        "/add",
        json={"taskid": "task1234", "params": {"test1": "1234","test2": "5678"}}
    )
    assert response.status_code == 400
