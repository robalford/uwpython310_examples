from unit_testing import is_palindrome

# Install pytest with python3 -m pip install pytest
# Run automated tests in directory with pytest command

# How to write tests for pytest

# With TDD, you write the tests first and then write the code that gets them to pass

def test_is_palindrome():
    known_palindromes = ["Racecar", "kayak", "RADAR", "Was it a cat I saw"]
    for string in known_palindromes:
        assert is_palindrome(string)

def test_not_palindrome():
    assert not is_palindrome("Some words")
