"""
Unit tests for the user module.
"""

from greet_user.get_user.user import username


def test_username() -> None:
    """
    Test username() returns string.
    """
    i_username = username()
    assert isinstance(i_username, str)
