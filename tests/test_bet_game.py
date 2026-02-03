import pytest
from app.bet_game import evaluate_bet


@pytest.mark.parametrize(
    "bet, no_bet, winner, expected",
    [
        # happy paths
        ("Mark", "Luis", "Mark", "WIN"),
        ("Mark", "Luis", "Luis", "LOSE"),

        # invalid winner (not one of the options)
        ("Rabbit", "Tortoise", "Goldfish", "INVALID_WINNER"),

        # invalid bet (both options same)
        ("Everyone", "Everyone", "Everyone", "INVALID_BET"),
        ("Cat", "Cat", "Dog", "INVALID_BET"),
    ]
)
def test_evaluate_bet(bet, no_bet, winner, expected):
    result = evaluate_bet(bet, no_bet, winner)
    assert result == expected, f"bet={bet}, no_bet={no_bet}, winner={winner}"
