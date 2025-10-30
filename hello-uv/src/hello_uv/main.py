from hello_uv.farewell import farewell
from hello_uv.greet import greet


def main() -> None:
    """Entry point for the program."""
    print(greet())
    print(farewell())


if __name__ == "__main__":
    # If file is run directly, call main()
    main()
