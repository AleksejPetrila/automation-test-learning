from jsonschema import validate


def assert_matches_schema(data: dict, schema: dict):
    # Will raise a clear exception if schema doesn't match (pytest will fail the test)
    validate(instance=data, schema=schema)
