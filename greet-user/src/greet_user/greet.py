"""
A simple Greeting program.

Using modern Python practices.
"""

from random import randint
from .get_user import user


def greet() -> str:
    """
    Generate a greeting message.

    For the message, use f-string to demo modern string formatting.
    Suffix a random number of '!' between 1 and 5. to the message.

    Returns:
        str: The greeting message.
    """
    message: str = "Hello, "
    count: int = randint(1, 5)
    return f"{message}{user.username()}{'!' * count}"
