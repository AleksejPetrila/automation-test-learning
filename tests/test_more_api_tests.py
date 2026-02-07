import pytest
import requests


@pytest.mark.api
def test_get_users_list(base_url, api_headers):
    r = requests.get(f"{base_url}/users", headers=api_headers, timeout=10)
    assert r.status_code == 200

    users = r.json()
    assert isinstance(users, list)
    assert len(users) >= 10

    first = users[0]
    assert first["id"] == 1
    assert first["username"] == "Bret"


@pytest.mark.api
def test_get_single_user_by_id(base_url, api_headers):
    r = requests.get(f"{base_url}/users/1", headers=api_headers, timeout=10)
    assert r.status_code == 200

    user = r.json()
    assert user["id"] == 1
    assert user["username"] == "Bret"
    assert "email" in user


@pytest.mark.api
def test_get_user_not_found(base_url, api_headers):
    r = requests.get(f"{base_url}/users/9999", headers=api_headers, timeout=10)
    # JSONPlaceholder returns 404 for missing resources
    assert r.status_code == 404


@pytest.mark.api
def test_username_value_not_alex(base_url, api_headers):
    r = requests.get(f"{base_url}/users", headers=api_headers, timeout=10)
    users = r.json()
    first_user = users[0]

    assert first_user["username"] != "Alex"


@pytest.mark.api
def test_username_value_not_alex(base_url, api_headers):
    r = requests.get(f"{base_url}/users/1", headers=api_headers, timeout=10)
    user = r.json()
    assert user["username"] != "Alex"


@pytest.mark.api
def test_create_post(base_url, api_headers):
    payload = {"userId": 1, "title": "Hello", "body": "From pytest"}
    r = requests.post(f"{base_url}/posts", json=payload, headers=api_headers, timeout=10)

    assert r.status_code == 201
    created = r.json()

    # JSONPlaceholder returns an id for the created resource
    assert "id" in created
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]
