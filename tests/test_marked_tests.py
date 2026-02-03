import pytest

@pytest.mark.smoke
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
    ]
)
def test_add_smoke(a, b, expected):
    assert a + b == expected


@pytest.mark.regression
@pytest.mark.parametrize(
    "d, e, expected",
    [
        (10, 5, 5),
        (3, 7, -4),
    ]
)
def test_subtract_regression(d, e, expected):
    assert d - e == expected