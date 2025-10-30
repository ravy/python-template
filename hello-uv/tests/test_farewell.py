"""
Unit tests for the hello_uv.farewell module.
Run with: uv run pytest
"""

from hello_uv.farewell import farewell


def test_farewell() -> None:
    """
    Test farewell() returns string 'Farewell!'.
    """
    assert farewell() == "Farewell!"
