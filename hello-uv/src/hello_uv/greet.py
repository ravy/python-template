"""
A simple Greeting program.

Using modern Python practices.
"""

import random


def greet() -> str:
    """
    Generate a greeting message.

    For the message, use f-string to demo modern string formatting.
    Suffix a random number of '!' between 1 and 5. to the message.

    Returns:
        str: The greeting message.
    """
    message: str = "Hello, uv"
    count: int = random.randint(1, 5)
    return f"{message}{'!' * count}"
