# Mom's Canning Timer — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/Moms-Canning-Timer
cd Moms-Canning-Timer
pip install -e .
```

No third-party runtime dependencies to install.

## Run it

```bash
python main.py                    # straight from the folder
canning-timer                     # via the console script
python -m moms_canning_timer      # as a module
```

## Tests and linting

```bash
pytest
pylint src/
```

CI runs pytest, pylint, and CodeQL on push; a separate workflow publishes to PyPI on release.
See [Testing](./testing.md).

## Where to make changes

| Change | Where |
|---|---|
| Countdown behaviour | `state.py` — no GUI knowledge belongs here |
| One burner's appearance or controls | `widget.py` |
| The window and grid layout | `app.py` |
| Packaging, entry points | `pyproject.toml` |

## Keep state free of tkinter

`state.py` is deliberately GUI-agnostic. That is what lets `tests/test_state.py` cover the
countdown logic with no display, and therefore what lets CI test it at all.

Reaching for a widget from inside state would work locally and break the suite in CI.

## Think before adding a dependency

The program has none at runtime, and that is a feature: it installs with no compiler, starts
instantly, and cannot be broken by an upstream release. Anything that would change that is
worth weighing against the convenience it buys.

## The default branch is `master`

Not `main`. Relevant when constructing links by hand — the old README had URLs pointing at
`/main/` that could never resolve.
