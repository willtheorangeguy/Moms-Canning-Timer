# Testing Documentation

This document describes the test suite for Mom's Canning Timer and how tests are integrated with GitHub Actions.

## Test Structure

The test suite is organized into three main test files:

### tests/test_main.py
Tests for the main timer functionality in `main.py`.

**Test Cases:**
- `test_timeStart1_callable()` - Verifies timeStart1 function is callable
- `test_timeStart1_execution()` - Tests timeStart1 runs without errors (with mocking)
- `test_timeStart2_callable()` - Verifies timeStart2 function is callable
- `test_timeStart2_execution()` - Tests timeStart2 runs without errors (with mocking)
- `test_timeStart3_callable()` - Verifies timeStart3 function is callable
- `test_timeStart3_execution()` - Tests timeStart3 runs without errors (with mocking)
- `test_timeStart4_callable()` - Verifies timeStart4 function is callable
- `test_timeStart4_execution()` - Tests timeStart4 runs without errors (with mocking)
- `test_timer_callable()` - Verifies timer function is callable
- `test_timer_creates_window()` - Tests timer creates a Tk window properly

**Testing Approach:**
- Uses `unittest.mock.patch` to mock `time.sleep()` and `print()` functions
- Uses threading to prevent tests from blocking for 15 minutes
- Verifies functions execute and call expected methods without full timer execution

### tests/test_init.py
Tests for the package initialization in `__init__.py`.

**Test Cases:**
- `test_all_attribute_exists()` - Verifies `__all__` attribute exists
- `test_all_contains_main()` - Verifies `__all__` contains 'main'
- `test_all_is_list()` - Verifies `__all__` is a list

### tests/test_entrypoint.py
Tests for the entry point module in `__main__.py`.

**Test Cases:**
- `test_main_module_exists()` - Verifies `__main__.py` file exists
- `test_main_has_correct_imports()` - Verifies correct import structure
- `test_main_has_docstring()` - Verifies proper documentation

## Running Tests

### Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install tkinter (if not already installed):
```bash
# On Ubuntu/Debian
sudo apt-get install python3-tk

# On macOS (using Homebrew)
brew install python-tk

# On Windows
# tkinter is usually included with Python installation
```

3. Run tests:
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_main.py

# Run specific test
pytest tests/test_main.py::TestTimer::test_timeStart1_callable
```

### In GitHub Actions

Tests run automatically on:
- Every push to any branch
- Every pull request

The GitHub Actions workflow:
1. Sets up Python environment
2. Installs system dependencies (python3-tk)
3. Installs Python dependencies from requirements.txt
4. Runs pytest with verbose output

See `.github/workflows/pytest.yml` for the complete workflow configuration.

## Test Dependencies

- **pytest** - Testing framework
- **unittest.mock** - Built-in Python mocking library
- **threading** - Built-in Python threading library for non-blocking tests
- **python3-tk** - System dependency for tkinter GUI framework

## Coverage

Current test coverage includes:
- All timer start functions (timeStart1-4)
- Main timer GUI function
- Package initialization
- Entry point module structure

## Best Practices

1. **Mocking Long-Running Operations**: Timer functions are designed to run for 15 minutes. Tests use mocking to verify logic without waiting.

2. **Threading for GUI Tests**: GUI operations can block test execution. Tests use threading with timeouts to prevent hanging.

3. **Testing Without Display**: Tests are designed to run in headless environments (like GitHub Actions) by mocking Tk window creation.

4. **Minimal Changes**: Tests verify behavior without modifying the original code, maintaining backward compatibility.

## Future Improvements

Potential areas for test expansion:
- Integration tests for complete timer workflows
- Performance tests for timer accuracy
- UI interaction tests with GUI automation tools
- Edge case testing (system sleep, interruptions, etc.)
- Code coverage reporting
