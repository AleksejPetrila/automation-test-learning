def test_sanity_check():
    assert 1 + 1 == 2


def test_addition_positive_numbers():
    # Arrange
    a = 10
    b = 5

    # Act
    result = a + b

    # Assert
    assert result == 15


def test_addition_with_zero():
    a = 7
    b = 0

    result = a + b

    assert result == 7


def test_addition_negative_numbers():
    a = -3
    b = -6

    result = a + b

    assert result == -9
