"""
Integration tests for the main module.
"""

from greet_user.main import main


def test_main_output(capsys, mock_username: None) -> None:
    """
    Test main() prints the correct output to stdout.
    """
    main()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].startswith("Hello, test-user")
    assert lines[1] == "Farewell test-user!"
