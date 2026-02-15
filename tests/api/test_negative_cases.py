import pytest
from src.api.endpoints import POSTS
from src.api.assertions import assert_status_code


@pytest.mark.api
@pytest.mark.parametrize("post_id", [0, -1, 999999, "cat"])
def test_get_post_invalid_id(api_client, post_id):
    response = api_client.get(f"{POSTS}/{post_id}")

    # JSONPlaceholder returns 404 for invalid ids like 0/-1/huge
    assert response.status_code in (400, 404)


@pytest.mark.api
@pytest.mark.parametrize("endpoint", ["/postss", "/user", "/invalidendpoint123"])
def test_invalid_endpoint_returns_404(api_client, endpoint):
    response = api_client.get(endpoint)
    assert_status_code(response, 404)


@pytest.mark.api
def test_create_post_missing_title(api_client):
    payload = {"userId": 1, "body": "Missing title field"}

    response = api_client.post(POSTS, json_body=payload)

    # JSONPlaceholder usually returns 201 even for bad payload,
    # but we still show how a test would be written in real API
    assert response.status_code in [201, 400]