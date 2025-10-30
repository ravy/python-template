"""
Unit tests for the farewell module.
"""

from greet_user.farewell import farewell


def test_farewell(mock_username: None) -> None:
    """
    Test farewell() returns string 'Farewell test-user!'.
    """
    assert farewell() == "Farewell test-user!"
