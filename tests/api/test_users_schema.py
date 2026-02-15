import pytest
from src.api.endpoints import USERS
from src.api.schema_validator import assert_matches_schema
from src.api.schemas import USER_SCHEMA


@pytest.mark.api
def test_get_single_user_schema(api_client):
    response = api_client.get(f"{USERS}/1")
    assert response.status_code == 200

    data = response.json()
    assert_matches_schema(data, USER_SCHEMA)
