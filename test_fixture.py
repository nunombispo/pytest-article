import pytest

@pytest.fixture
def sample_numbers():
    """Create a list of numbers for testing."""
    return [1, 2, 3, 4, 5]

def test_sum_numbers(sample_numbers):
    total = sum(sample_numbers)
    assert total == 15

def test_list_length(sample_numbers):
    assert len(sample_numbers) == 5