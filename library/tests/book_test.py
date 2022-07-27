
from fastapi.testclient import TestClient

from library.main import app

client = TestClient(app)


def test_create_book(set_up_book):
    response = client.post("/user/2/book", json=set_up_book)
    assert response.status_code == 200
    assert response.json()["title"] == "1984"
    assert response.json()["author"] == "George Orwell"
    assert response.json()["owner_id"] == "2"
    assert response.json()["id"] == "2"

