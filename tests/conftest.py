import pytest


@pytest.fixture
def sample_numbers():
    return 10, 5


@pytest.fixture
def list_of_suspects():
    return "Alice", "Bob", "Claire", "Daniel", "Evil Mr. Jenkins"


@pytest.fixture(scope="function")
def sample_numbers_with_cleanup():
    print("\n[SETUP] Preparing numbers second test")
    numbers = (5, 6)

    yield numbers

    print("\n[TEARDOWN] Finishing the second test")


@pytest.fixture(scope="module")
def scoped_numbers():
    print("\n[SETUP] module fixture")
    yield (4, 6)
    print("\n[TEARDOWN] module fixture")
