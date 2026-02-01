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


def test_the_suspect(list_of_suspects):
    a, b, c, d, e = list_of_suspects
    released = c
    assert released != "Evil Mr. Jenkins"


def test_addition_with_fixtures(sample_numbers):
    a, b = sample_numbers
    result = a + b
    assert result == 15


def test_subtraction(sample_numbers):
    a, b = sample_numbers
    result = a - b
    assert result == 5


def test_multiplication(sample_numbers):
    a, b = sample_numbers
    result = a * b
    assert result == 50


def test_division(sample_numbers):
    a, b = sample_numbers
    result = b / a
    assert result == 0.5


def test_addition_with_cleanup(sample_numbers_with_cleanup):
    a, b = sample_numbers_with_cleanup
    result = a + b
    assert result == 11


def test_second_test_with_cleanup(sample_numbers_with_cleanup):
    a, b = sample_numbers_with_cleanup
    result = a - b
    assert result == -1


def test_add(scoped_numbers):
    a, b = scoped_numbers
    assert a + b == 10


def test_multiply(scoped_numbers):
    a, b = scoped_numbers
    assert a * b == 24

