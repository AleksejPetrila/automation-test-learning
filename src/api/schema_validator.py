from jsonschema import validate
from jsonschema.exceptions import ValidationError


def _format_path(err: ValidationError) -> str:
    """Turns jsonschema error path into a nice dotted path like: address.zipcode"""
    if not err.path:
        return "(root)"
    return ".".join(str(p) for p in err.path)


def assert_matches_schema(data: dict, schema: dict, *, name: str = "schema"):
    """
    Validates JSON data against a JSON Schema.
    If it fails, raises AssertionError with a readable message for terminal + HTML report.
    """
    try:
        validate(instance=data, schema=schema)
    except ValidationError as err:
        path = _format_path(err)
        expected = err.schema.get("type") if isinstance(err.schema, dict) else None

        # Keep message readable; include a short view of the failing value when possible
        got_value = err.instance
        got_preview = repr(got_value)
        if len(got_preview) > 200:
            got_preview = got_preview[:200] + "...(truncated)"

        raise AssertionError(
            f"Schema validation failed ({name})\n"
            f"- Path: {path}\n"
            f"- Problem: {err.message}\n"
            f"- Expected: {expected}\n"
            f"- Got: {got_preview}\n"
        ) from None
