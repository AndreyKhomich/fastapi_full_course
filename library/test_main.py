from fastapi.testclient import TestClient
from .hashing import Hash

from .main import app

client = TestClient(app)



def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Andrei",
        "email": "Andrei@gmail.com",
        "books": [{'author': 'George Orwell', 'title': '1984'}]
    }


def test_get_single_book():
    response = client.post("/book/1")
    assert response.status_code == 201
    assert response.json() == {
        "title": "1984",
        "author": "George Orwell",
        "reader": {
            "name": "Andrei",
            "email": "andrei@gmail.com",
            "books": [
                {
                    "title": "1984",
                    "author": "George Orwell"
                },
                {
                    "title": "BOOOOOK",
                    "author": "Vladimir Lenin"
                },
                {
                    "title": "Book Dear Book",
                    "author": "None None"
                }
            ]
        }
    }


