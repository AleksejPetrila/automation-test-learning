POST_REQUIRED_KEYS = ["id", "userId", "title", "body"]

def assert_post_has_required_fields(post_data: dict):
    assert "id" in post_data, "Missing 'id' in response"
    assert "userId" in post_data, "Missing 'userId' in response"
    assert "title" in post_data, "Missing 'title' in response"
    assert "body" in post_data, "Missing 'body' in response"


def assert_post_schema(post_data: dict):
    assert_has_keys(post_data, POST_REQUIRED_KEYS)
    assert isinstance(post_data["id"], int), f"id should be int, got {type(post_data['id'])}"
    assert isinstance(post_data["userId"], int), f"userId should be int, got {type(post_data['userId'])}"
    assert isinstance(post_data["title"], str), f"title should be str, got {type(post_data['title'])}"
    assert isinstance(post_data["body"], str), f"body should be str, got {type(post_data['body'])}"


def assert_post_values(post_data: dict, expected_data: dict):
    for key, expected_value in expected_data.items():
        assert post_data.get(key) == expected_value, f"Expected {key}={expected_value}, got {post_data.get(key)}"


def assert_status_code(response, expected: int):
    actual = response.status_code
    assert actual == expected, (
        f"Expected status code {expected}, got {actual}. "
        f"Response body: {response.text}"
    )


def assert_has_keys(data: dict, keys: list):
    for key in keys:
        assert key in data, f"Missing key '{key}' in response. Got keys: {list(data.keys())}"


