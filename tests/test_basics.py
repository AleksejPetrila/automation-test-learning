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


def test_good_bad_balance_main():
    good = 10
    bad = 1

    balance = good - bad

    assert balance >= 2


def test_the_suspect():
    a = "Mary"
    b = "Billy"
    c = "Mittens"
    d = "An evil mr. Jenkins"

    released = c

    assert released != "An evil mr. Jenkins"


def test_addition_with_fixtures(sample_numbers):
    a, b = sample_numbers
    result = a + b
    assert result == 15
