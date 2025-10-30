"""
Unit tests for the greet module.
"""

from greet_user.greet import greet


def test_greet_hello_prefix(mock_username: None) -> None:
    """
    Test greet() returns string that starts with 'Hello, test-user'.
    """
    greeting = greet()
    assert greeting.startswith("Hello, test-user")


def test_greet_hello_suffix(mock_username: None) -> None:
    """
    Test greet() string ends with 1–5 exclamation marks.
    """
    greeting = greet()
    suffix = greeting[len("Hello, test-user") :]
    assert 1 <= len(suffix) <= 5
    assert set(suffix) == {"!"}
