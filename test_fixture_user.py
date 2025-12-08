import pytest

@pytest.fixture
def sample_user():
    """Create a sample user for testing."""
    return {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }

def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"

def test_user_age(sample_user):
    assert sample_user["age"] == 30