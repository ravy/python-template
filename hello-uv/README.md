# Hello uv

![CI](https://github.com/ravy/python-template/.github/actions/workflows/ci-hello-uv.yaml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

## Introduction

A Barebones Hello Python project.

Demonstrate modern pythonic practices like
- unit-tests
- type hints
- docstrings
- formatted strings
- clean project structure
- linting
- formatting

**Goals**:
- Get you comfortable with running, testing a Python project.
- Give a starter modern python project-template or scaffold you can build upon.

**Tech Stack**:
- python as language
- [uv](https://docs.astral.sh/uv/) for python and pkg management
- pytest for tests
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting

**Time**: 5-10 minutes

### Project Structure

```
hello-uv/
├── pyproject.toml        # Config for uv, pytest, and project metadata
├── README.md             # You're reading it!
├── .gitignore            # Ignores junk like .venv
├── src/
│   └── hello_uv
│       ├── __init__.py   # Makes 'hello_uv' a package (with docstring)
│       ├── greet.py      # The script for greet()
│       ├── farewell.py   # The script for farewell()
│       └── main.py       # The main script
└── tests/
    ├── test_greet.py     # test file for greet.py
    └── test_farewell.py  # test file for farewell.py
```

## Setup

First Clone the repo and cd into dir `hello-uv`:

1. **Install uv** (if not already):
   Follow the [official guide](https://docs.astral.sh/uv/getting-started/installation/).

2. **Sync Dependencies**:
   uv will create a virtual environment (`.venv`) and install everything from `pyproject.toml`.
   ```
   uv sync
   ```
   - Note: Run this anytime you add deps with `uv add <package>`.
   - Note: If you did not have python, uv will install it now.

3. **Verify Setup**:
   Run `uv run python -V` to print python version and confirm your env is active.

## How to Use

- **Run the Greeting**:
  Execute script directly with uv (auto-uses the virtual env):
  ```
  uv run hello
  ```

  Output:
  ```
  Hello, uv!!!
  Farewell!
  ```
  (Note: The number of exclamation marks in the greeting may vary.)

## Testing

Use pytest for simple, readable tests.

- **Run All Tests**:
  ```
  uv run pytest
  ```
  - Output: Something like `3 passed in 0.01s`.
  - This runs files in the `tests/` directory automatically.
  - For Verbose Output use `uvx pytest -v`

- **Code Coverage**:
  Generate a coverage report to see which lines of code your tests exercise.
  ```
  uv run pytest --cov=src/hello_uv
  ```

## Static Analysis

This project uses `ruff` for linting and formatting. While you can run these manually, the project is also configured to run them automatically before each commit.

### **Manual Checks**

From project directory root
	1.	Run `uv run ruff format` to fix what can be auto-fixed.
	2.	Run `uv run ruff check` to catch remaining issues that require manual attention.

### **Automated Quality Checks**

This project uses pre-commit hooks to ensure code quality and consistency automatically. Before you commit any changes, `ruff` will automatically format your code and check for errors.

To enable this, you first need to install the hooks by running:
```
uv run pre-commit install
```
After this one-time setup, the checks will run automatically on every `git commit`.

#### Github CI/CD
This project includes a Continuous Integration (CI) pipeline using GitHub Actions to automatically ensure code quality.

## Next Steps

### **Version Control**

1. **Rename the folder** (recommended):
```
mv hello-uv new-awesome-name
cd new-awesome-name
```

2. **Initialize git repo:**
```
git init
git checkout -b master  # 'master' as default branch
```

3. **Update project metadata:**
- Rename the project in pyproject.toml:
```
[project]
name = "new-project-name"
authors = [{ name = "Your Name", email = "your@email.com" }]
```

4. **Stage and commit changes:**
```
git add .
git commit -m "Initial project"
```

5. **Push to your own GitHub repo:**
- Create repo with GitHub CLI:
```
gh repo create new-project-name --public --source=. --push
```

## Conclusion

**Star this repo**:
- Found this helpful? Learned something? Star ⭐️ it.
- Watch to be upto date with the latest trends.

**Questions?**
- Open an issue or
- ping me on X (@_ravy)

Happy coding! 🚀
