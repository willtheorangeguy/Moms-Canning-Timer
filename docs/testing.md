# Testing Documentation

This document describes the test suite for Mom's Canning Timer and how tests are
integrated with GitHub Actions.

## Test Structure

The package separates pure countdown logic (`moms_canning_timer.state`) from the
tkinter GUI (`moms_canning_timer.widget`, `moms_canning_timer.app`). This makes
the core logic testable without a display, while the GUI tests skip
automatically when no display is available.

### tests/test_state.py
Tests for `TimerState`, the GUI-free countdown logic. Always runs (no display
needed).

- Duration setting and clamping to the 1–180 minute range.
- Start / pause / resume / reset transitions.
- `tick()` decrements and fires "done" exactly once at zero.
- `fraction_done()` endpoints and `display()` (`MM:SS`) formatting.

### tests/test_widget.py
Tests for the `CircularTimer` widget. Skipped when no Tk display is available.

- Initial display and spinbox-driven duration.
- Start, Pause/Resume toggle, and Reset behaviour.
- Finish path fires the injected alert callback (no real dialog in tests).

### tests/test_app.py
Tests for `build_window()`. Skipped when no Tk display is available.

- Window title.
- Four `CircularTimer` instances created.
- Timers placed in a 2x2 grid (`{(0,0), (0,1), (1,0), (1,1)}`).

### tests/test_package.py
Tests for package metadata: `__version__`, `__all__` exports, and that the
`canning-timer` entry point (`moms_canning_timer.app:main`) is callable.

### tests/gui_support.py
Helper that detects whether a Tk display is available, used by the GUI tests via
`@unittest.skipUnless`.

## Running Tests

### Locally

1. Install the package with test extras:
```bash
pip install -e .[test]
```

2. Install tkinter (if not already installed):
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (using Homebrew)
brew install python-tk

# On Windows, tkinter ships with the official Python installer.
```

3. Run tests:
```bash
# Run all tests
pytest

# Verbose
pytest -v

# A single file or test
pytest tests/test_state.py
pytest tests/test_state.py::TestTimerState::test_display_formatting
```

On headless machines (no display), the widget and window tests are skipped and
the logic tests still run.

### In GitHub Actions

Tests run on every push and pull request across Python 3.9–3.13. The workflow
installs `python3-tk` and `xvfb`, installs the package, and runs the suite under
`xvfb-run` so the GUI tests get a virtual display. See
`.github/workflows/pytest.yml`.

## Test Dependencies

- **pytest** — test runner.
- **unittest** — assertions and skip decorators (standard library).
- **python3-tk** — tkinter, for the GUI tests.
- **xvfb** — virtual framebuffer used in CI to run GUI tests headlessly.
