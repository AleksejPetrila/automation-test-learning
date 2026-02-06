import pytest
import requests


@pytest.mark.notapi
def test_get_users_list():
    response = requests.get("https://reqres.in/api")

    assert response.status_code == 200

    body = response.json()
    assert "data" in body
    assert len(body["data"]) > 0


BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users", timeout=10)

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0

    first_user = body[0]
    assert "id" in first_user
    assert "email" in first_user
    assert first_user["username"] == "Bret"
