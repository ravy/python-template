"""
Configuration for pytest.
"""

from typing import Generator
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_username() -> Generator[None, None, None]:
    """
    Fixture to mock the username function.
    """
    with patch("greet_user.get_user.user.username") as mock:
        mock.return_value = "test-user"
        yield
