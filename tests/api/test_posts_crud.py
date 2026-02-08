import pytest
from src.api.endpoints import POSTS
from src.api.assertions import assert_post_has_required_fields, assert_post_values


@pytest.mark.api
def test_update_post_put(api_client):
    post_id = 1
    payload = {"id": post_id, "title": "Updated title", "body": "Updated body", "userId": 1}

    response = api_client.put(f"{POSTS}/{post_id}", json_body=payload)

    assert response.status_code == 200

    data = response.json()
    assert_post_has_required_fields(data)
    assert_post_values(data, payload)


@pytest.mark.api
def test_update_post_patch(api_client):
    post_id = 1
    payload = {"title": "Partially updated title"}

    response = api_client.patch(f"{POSTS}/{post_id}", json_body=payload)

    assert response.status_code == 200

    data = response.json()
    assert_post_has_required_fields(data)
    assert_post_values(data, payload)


@pytest.mark.api
def test_delete_post(api_client):
    post_id = 1

    response = api_client.delete(f"{POSTS}/{post_id}")

    assert response.status_code == 200
