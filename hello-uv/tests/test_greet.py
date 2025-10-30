"""
Unit tests for the hello_uv.greet module.
Run with: uv run pytest
"""

from hello_uv.greet import greet


def test_greet_hello_prefix() -> None:
    """
    Test greet() returns string that starts with 'Hello, uv'.
    """
    greeting = greet()
    assert greeting.startswith("Hello, uv")


def test_greet_hello_suffix() -> None:
    """
    Test greet() string ends with 1–5 exclamation marks.
    """
    greeting = greet()
    suffix = greeting[len("Hello, uv") :]
    assert 1 <= len(suffix) <= 5
    assert set(suffix) == {"!"}
