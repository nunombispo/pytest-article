# pytest Beginner's Guide

A beginner-friendly guide to learning pytest, Python's most popular testing framework. This repository contains a comprehensive article that will teach you everything you need to know to get started with testing in Python.

If these scripts were useful to you, consider donating to support the Developer Service Blog: https://buy.stripe.com/bIYdTrggi5lZamkdQW

## 📚 What's Inside

This repository includes:

- **Example code files** - Working examples you can run and experiment with
- **Requirements file** - Dependencies needed to run the examples

## 🚀 Quick Start

### 1. Install pytest

```bash
pip install pytest
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

### 2. Verify Installation

```bash
pytest --version
```

### 3. Run the Example Tests

```bash
pytest
```

This will automatically discover and run all test files in the repository.

## 📁 Project Structure

```
pytest-article/
├── README.md                 # This file
├── requirements.txt         # Python dependencies
├── calculator.py            # Example function to test
├── test_calculator.py       # Example tests
└── test_fixture.py          # Example using fixtures
```

## 💡 Example Code

The repository includes working examples:

**`calculator.py`** - A simple function to test:
```python
def add_numbers(a, b):
    """Add two numbers together."""
    return a + b
```

**`test_calculator.py`** - Tests for the calculator:
```python
from calculator import add_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5
```

Run the tests with:
```bash
pytest test_calculator.py
```

## 🧪 Running Tests

Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest test_calculator.py
```

Run with verbose output:
```bash
pytest -v
```

Run in quiet mode:
```bash
pytest -q
```

## 📝 Requirements

- Python 3.7 or higher
- pytest 9.0.2 (or latest version)

## 🤝 Contributing

Found an error or want to improve the article? Feel free to open an issue or submit a pull request!

## 📄 License

This project is open source and available for educational purposes.

## 🔗 Resources

- [Official pytest Documentation](https://docs.pytest.org/)
- [pytest on GitHub](https://github.com/pytest-dev/pytest)

---

**Happy Testing! 🎉**

