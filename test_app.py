import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_contanct_page(client):
    response = client.get("/") 
    assert b"its" in response.data # noqa
    assert b"working" in response.data # noqa
        