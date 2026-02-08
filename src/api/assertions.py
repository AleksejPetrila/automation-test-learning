def assert_post_has_required_fields(post_data: dict):
    assert "id" in post_data, "Missing 'id' in response"
    assert "userId" in post_data, "Missing 'userId' in response"
    assert "title" in post_data, "Missing 'title' in response"
    assert "body" in post_data, "Missing 'body' in response"


def assert_post_values(post_data: dict, expected_data: dict):
    """
    Validates that response contains expected values.
    Only checks keys that exist in expected_data.
    """
    for key, expected_value in expected_data.items():
        assert post_data[key] == expected_value, f"Expected {key}={expected_value}, but got {post_data[key]}"
