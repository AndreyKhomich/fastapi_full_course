import pytest

from library.hashing import Hash
from .main import app
from fastapi.testclient import TestClient
from .oath2 import get_current_user


@pytest.fixture
def set_up_user():
    user = {
        "id": "123",
        "name": "Sasha",
        "email": "sasha@gmail.com",
        "password": Hash.bcrypt("Sasha")
    }
    return user


@pytest.fixture
def set_up_book():
    book = {
        "title": "1984",
        "author": "George Orwell",
        "user_id": "1"
    }
    return book


@pytest.fixture
def user():
    """
    Return an API Client
    """
    app.dependency_overrides = {}
    return TestClient(app)


@pytest.fixture
def user_authenticated():
    """
    Returns an API client which skips the authentication
    """
    def skip_auth():
        pass
    app.dependency_overrides[get_current_user] = skip_auth
    return TestClient(app)





