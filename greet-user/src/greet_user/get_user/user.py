import getpass


def username() -> str:
    """Return the current user's username."""
    return getpass.getuser()
