"""
A simple Farewell program.

Using modern Python practices.
"""

from .get_user import user


def farewell() -> str:
    """
    Generate a farewell message.

    Returns:
        str: The farewell message.
    """
    return f"Farewell {user.username()}!"
