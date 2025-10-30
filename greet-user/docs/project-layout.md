# Project Layout

The project is structured as follows:

```
.
├── .gitignore
├── .pre-commit-config.yaml
├── AGENTS.md
├── mkdocs.yml
├── pyproject.toml
├── README.md
├── uv.lock
├── .pytest_cache
├── .ruff_cache
├── .venv
├── docs
│   └── index.md
├── site
├── src
│   └── greet_user
│       ├── __init__.py
│       ├── farewell.py
│       ├── greet.py
│       ├── main.py
│       ├── __pycache__
│       └── get_user
│           ├── __init__.py
│           ├── user.py
│           └── __pycache__
└── tests
    ├── conftest.py
    ├── test_farewell.py
    ├── test_greet.py
    ├── test_main.py
    ├── test_user.py
    └── __pycache__
```

- **`.gitignore`**: A list of files and directories that Git should ignore.
- **`.pre-commit-config.yaml`**: Configuration for pre-commit hooks.
- **`AGENTS.md`**: Documentation for the agents.
- **`mkdocs.yml`**: Configuration for the MkDocs documentation.
- **`pyproject.toml`**: A single file for all your project's configuration.
- **`README.md`**: The main README file for the project.
- **`uv.lock`**: A lock file for the uv package manager.
- **`.pytest_cache`**: Cache directory for pytest.
- **`.ruff_cache`**: Cache directory for ruff.
- **`.venv`**: The virtual environment for the project.
- **`docs`**: The documentation for the project.
- **`site`**: The generated documentation site.
- **`src`**: The source code for the project.
- **`tests`**: The tests for the project.
