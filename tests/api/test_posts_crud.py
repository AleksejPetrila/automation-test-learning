import pytest
from src.api.endpoints import POSTS
from src.api.assertions import assert_status_code, assert_post_schema, assert_post_values
from src.test_data.posts import put_post_payload
from src.api.schema_validator import assert_matches_schema
from src.api.schemas import POST_SCHEMA


@pytest.mark.api
@pytest.mark.smoke
def test_update_post_put(api_client):
    post_id = 1
    payload = put_post_payload(post_id=post_id)

    response = api_client.put(f"{POSTS}/{post_id}", json_body=payload)

    assert_status_code(response, 200)

    data = response.json()
    assert_post_schema(data)
    assert_post_values(data, payload)


@pytest.mark.api
@pytest.mark.smoke
def test_update_post_patch(api_client):
    post_id = 1
    payload = {"title": "Partially updated title"}

    response = api_client.patch(f"{POSTS}/{post_id}", json_body=payload)

    assert_status_code(response, 200)

    data = response.json()
    assert_post_schema(data)
    assert_post_values(data, payload)


@pytest.mark.api
@pytest.mark.regression
def test_delete_post(api_client):
    post_id = 1
    response = api_client.delete(f"{POSTS}/{post_id}")
    assert_status_code(response, 200)


@pytest.mark.api
@pytest.mark.regression
def test_get_single_post_schema(api_client):
    response = api_client.get(f"{POSTS}/1")
    assert response.status_code == 200

    data = response.json()
    assert_matches_schema(data, POST_SCHEMA)


@pytest.mark.api
@pytest.mark.regression
def test_get_posts_list_schema(api_client):
    response = api_client.get(POSTS)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # validate first 3 items (enough to prove structure)
    for post in data[:3]:
        assert_matches_schema(post, POST_SCHEMA)
