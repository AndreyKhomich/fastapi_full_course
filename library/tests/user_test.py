
from fastapi.testclient import TestClient

from library.main import app

client = TestClient(app)


def test_create_user(set_up_user):
    response = client.post("/user/", json=set_up_user)
    assert response.status_code == 200
    assert response.json()["name"] == "Sasha"
    assert response.json()["email"] == "sasha@gmail.com"


def test_get_user(set_up_user):
    response = client.get("/user/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Andrei"
    assert response.json()["email"] == "andrei@gmail.com"
    assert response.json()["books"] == []



