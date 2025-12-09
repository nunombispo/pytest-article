from calculator import add_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5

def test_add_numbers_wrong():
    result = add_numbers(2, 3)
    assert result == 10  # This is wrong!