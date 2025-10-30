# Greet User

![CI](https://github.com/ravy/python-template/.github/actions/workflows/ci-greet-user.yaml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

## Introduction

A Simple Python project.

Demonstrate modern pythonic practices like
- unit testing
- docstrings
- formatted strings
- clean project structure
- linting
- formatting
- pre-commit hooks
- github CI/CD

**Goals**:
- Get you comfortable with running, testing a Python project.
- Give a starter modern python project-template or scaffold you can build upon.

**Tech Stack**:
- python as language
- [uv](https://docs.astral.sh/uv/) for python and build management
- pytest for tests
- pytest-cov for code-coverage
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- pre-commit for git pre-commit hooks
- Github CI/CD to ensure code quality

**Time**: 5-10 minutes

### Project Structure

```
greet-user/
├── pyproject.toml        # Config for project metadata
├── README.md             # You're reading it!
├── .gitignore            # git ignore file
├── src/                  # source directory
│   └── greet_user        # main package
│       ├── __init__.py   # package initialization
│       ├── greet.py      # greet module
│       ├── farewell.py   # farewell module
│       ├── main.py       # The main script
│       └── get_user      # sub package
│           ├── __init__.py
│           └── user.py   # user module
└── tests/
│   ├── conftest.py       # pytest fixtures
│   ├── test_greet.py     # test file for greet.py
│   ├── test_farewell.py  # test file for farewell.py
│   ├── test_user.py      # test file for user.py
└── docs/                 # Documentation
    └── index.md
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
  uv run greet
  ```

  Output:
  ```
  Hello, {user}!!!
  Farewell {user}!
  ```
  (Note: The number of exclamation marks in the greeting may vary.)

## Testing

Use pytest for simple, readable tests.

- **Run All Tests**:
  ```
  uv run pytest
  ```
  - Output: Something like `5 passed in 0.01s`.
  - This runs files in the `tests/` directory automatically.
  - For Verbose Output use `uvx pytest -v`

- **Code Coverage**:
  Generate a coverage report to see which lines of code your tests exercise.
  ```
  uv run pytest --cov=src/greet_user
  ```

## Static Analysis

This project uses `ruff` for linting and formatting. While you can run these manually, the project is also configured to run them automatically before each commit.

### **Automated Quality Checks**

#### Formatting and Linting
This project uses pre-commit hooks to ensure code quality and consistency automatically. Before you commit any changes, `ruff` will automatically format your code and lint for errors.

#### Github CI/CD
This project includes a Continuous Integration (CI) pipeline using GitHub Actions to automatically ensure code quality.

## Documentation

This project uses [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme for documentation.

- **Serve Documentation Locally**:
  ```
  uv run mkdocs serve
  ```
  Open your browser to `http://127.0.0.1:8000` to view the documentation.

- **Build Documentation**:
  ```
  uv run mkdocs build
  ```
  This will generate a `site/` directory containing the static HTML documentation.

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
