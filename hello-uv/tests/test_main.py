"""
Integration tests for the hello_uv.main module.
Run with: uv run pytest
"""

from hello_uv.main import main


def test_main_output(capsys) -> None:
    """
    Test main() prints the correct output to stdout.
    """
    main()
    captured = capsys.readouterr()
    assert captured.out.startswith("Hello, uv")
    assert "Farewell!\n" in captured.out
