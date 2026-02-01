import pytest


@pytest.fixture
def sample_numbers():
    return 10, 5


@pytest.fixture
def list_of_suspects():
    return "Alice", "Bob", "Claire", "Daniel", "Evil Mr. Jenkins"
