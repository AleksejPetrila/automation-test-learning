import pytest
from src.api.endpoints import POSTS


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize(
    "payload, expected_statuses, case",
    [
        # Missing required fields (typical real API -> 400)
        ({"userId": 1, "body": "no title"}, (201, 400), "missing_title"),
        ({"userId": 1, "title": "no body"}, (201, 400), "missing_body"),
        ({"title": "no userId", "body": "text"}, (201, 400), "missing_userId"),

        # Wrong types (typical real API -> 400)
        ({"userId": "one", "title": "t", "body": "b"}, (201, 400), "userId_wrong_type"),
        ({"userId": 1, "title": 123, "body": "b"}, (201, 400), "title_wrong_type"),
        ({"userId": 1, "title": "t", "body": 999}, (201, 400), "body_wrong_type"),

        # Empty payload
        ({}, (201, 400), "empty_payload"),

        # Extra field (many real APIs allow it, some reject -> 400)
        ({"userId": 1, "title": "t", "body": "b", "extra": "field"}, (201, 400), "extra_field"),
    ],
)
def test_create_post_negative_payloads(api_client, payload, expected_statuses, case):
    response = api_client.post(POSTS, json_body=payload)

    # JSONPlaceholder is a fake API and often returns 201 even for invalid payloads.
    # In real-world APIs, most of these cases should return 400 with validation errors.
    assert response.status_code in expected_statuses, (
        f"Case '{case}' failed. Expected one of {expected_statuses}, got {response.status_code}. "
        f"Response body: {response.text}"
    )