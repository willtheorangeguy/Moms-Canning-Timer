# CLAUDE.md

## Project Overview

Mom's Canning Timer is a Python/tkinter desktop application providing customizable 15-minute stove-top timers for food preservation. Version 0.3.0 (Alpha). Licensed under MIT.

## Repository Structure

```
main.py              # Main application – GUI and timer logic
__init__.py          # Package init
__main__.py          # Entry point for `python -m` execution
setup.py             # Package setup (console_scripts entry point)
pyproject.toml       # Build system config
requirements.txt     # Dependencies (pytest)
timer/               # Timer module (example/counter)
tests/               # pytest test suite
docs/                # User-facing documentation
.github/workflows/   # CI: pytest, pylint, CodeQL, PyPI publish
```

## Commands

```bash
# Run the app
python main.py

# Run tests
pytest -v

# Run linter
pylint $(git ls-files '*.py')

# Install dependencies
pip install -r requirements.txt
```

## CI/CD

All workflows are GitHub Actions in `.github/workflows/`:
- **pytest.yml** – runs `pytest -v` on push and PR (requires `python3-tk` system package)
- **pylint.yml** – runs pylint on push (Python 3.9)
- **codeql-analysis.yml** – weekly security analysis + on push/PR
- **push-to-pypi.yml** – builds and publishes to PyPI on release

## Code Conventions

- **Indentation:** 4 spaces, no tabs
- **Comments:** Comment all functions and code blocks (project convention per CONTRIBUTING.md)
- **Function naming:** camelCase (e.g., `timeStart1`, `timeStart2`)
- **Global variables:** UPPER_CASE with pylint disable comments where needed
- **Versioning:** Semantic Versioning
- **Style:** Must pass pylint; Black formatting via DeepSource

## Architecture

- `main.py` contains a `timer()` function that creates the tkinter GUI with four burner timers
- Each timer function (`timeStart1` through `timeStart4`) runs a 15-minute countdown
- Console entry point: `canning-timer = main:timer` (defined in setup.py)
- `__main__.py` imports and calls `timer()` for `python -m` invocation

## Testing

Tests live in `tests/` and use pytest:
- `test_main.py` – unit tests for main application logic
- `test_entrypoint.py` – tests for `__main__.py`
- `test_init.py` – tests for `__init__.py`

## Dependencies

- **Runtime:** tkinter (built-in with Python 3.9+)
- **Dev:** pytest, pylint
- **Build:** setuptools, wheel
