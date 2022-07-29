import json

from library import models
from library.hashing import Hash


user = {
    "id": 1,
    "name": "testuser",
    "email": "testuser@gmail.com",
    "password": Hash.bcrypt("testuser")
}


def test_create_user(client):
    response = client.post("/user/", json.dumps(user))
    assert response.status_code == 200
    assert response.json()["name"] == "testuser"
    assert response.json()["email"] == "testuser@gmail.com"


def test_get_user(client, session):
    new_user = models.User(id=1, name="Sergei", email="sergei@gmail.com", password="Sergei")
    session.add(new_user)
    session.commit()
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Sergei"
    assert response.json()["email"] == "sergei@gmail.com"
    assert response.json()["books"] == []




