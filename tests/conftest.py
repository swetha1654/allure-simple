import pytest


@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers for tests."""
    return {"a": 10, "b": 5, "c": 0}


@pytest.fixture
def sample_list():
    """Fixture providing a sample list of numbers."""
    return [1, 2, 3, 4, 5, 6]
