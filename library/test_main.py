import json

from fastapi.testclient import TestClient
from .hashing import Hash
import pytest

from .test_database import app

client = TestClient(app)

book_request = {
    "title": "1984",
    "author": "George Orwell",
}

book_response = {
    "title": "1984",
    "user_id": 1,
    "author": "George Orwell",
    "id": 2
}


@pytest.fixture
def set_up_user():
    user = {
        "id": "1",
        "name": "Andrei",
        "email": "andrei@gmail.com",
        "password": Hash.bcrypt("Andrei")
    }
    return user


@pytest.fixture
def set_up_book():
    book = {
        "id": "1",
        "title": "1984",
        "author": "George Orwell",
        "user_id": "1"
    }
    return book


def test_create_user(set_up_user):
    response = client.post("/user/", json=set_up_user)
    assert response.status_code == 200
    assert response.json()["name"] == "Andrei"
    assert response.json()["email"] == "andrei@gmail.com"


def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Andrei"
    assert response.json()["email"] == "andrei@gmail.com"
    assert response.json()["books"] == [{'author': 'George Orwell', 'title': '1984'}]


# Тест не выполняется, выпадает ошибка  TypeError: Object of type function is not JSON serializable
def test_create_book():
    response = client.post("/book/user/1/book/", json=set_up_book)
    assert response.status_code == 200
    assert response.json()["title"] == "1984"
    assert response.json()["author"] == "George Orwell"
    assert response.json()["user_id"] == "1"


