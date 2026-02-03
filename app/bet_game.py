def evaluate_bet(bet: str, no_bet: str, winner: str) -> str:
    """
    Evaluate the bet result.

    Returns:
        "WIN"            - winner matches bet
        "LOSE"           - winner matches no_bet
        "INVALID_WINNER" - winner matches neither option
        "INVALID_BET"    - bet and no_bet are the same
    """
    if bet == no_bet:
        return "INVALID_BET"

    if winner == bet:
        return "WIN"

    if winner == no_bet:
        return "LOSE"

    return "INVALID_WINNER"