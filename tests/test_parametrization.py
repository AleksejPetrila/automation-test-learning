import pytest


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 7, 12),
        (-1, -2, -3),
        (10, 0, 10),
    ]
)
def test_addition_parametrized(a, b, expected):
    result = a + b
    assert result == expected


@pytest.mark.parametrize(
    "bet, no_bet, winner",
    [
        ("Mark", "Luis", "Luis"),
        ("Cat", "Dog", "Cat"),
        ("Rabbit", "Tortoise", "Goldfish"),
        ("Everyone", "Everyone", "Everyone"),
    ]
)
def test_check_bets(bet, no_bet, winner):
    result = winner
    assert result == bet
