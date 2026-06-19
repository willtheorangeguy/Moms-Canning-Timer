# Changelog

## [v1.0.0](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/tag/v1.0.0)

### Added

- Working GUI: four timers in a 2x2 stove grid, each with a circular progress ring.
- Per-timer duration entry plus Start, Pause/Resume, and Reset controls.
- Bell + popup alert when a timer finishes.
- `src/` layout package `moms_canning_timer` with GUI-free `TimerState` logic.
- Tests for timer logic, widget, window layout, and packaging.

### Changed

- Replaced the blocking `time.sleep` console loops with a non-blocking
  tkinter `after()` countdown.
- Restructured into an installable package; packaging consolidated into
  `pyproject.toml`.
- CI runs the suite across Python 3.9–3.13 under `xvfb`; PyPI publishing uses
  trusted publishing (OIDC).

## [v0.3.0](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/tag/v0.3.0)

### Added

- PyTest tests.

## [v0.2.1](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/tag/v0.2.1)

### Changed

- PyPI package.

## [v0.2.0](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/tag/v0.2.0)

### Added

- PyPI package.

## [v0.1.0](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/tag/v0.1.0)

### Added

- Initial program.
- Community documentation.

### Changed

- `README` and documentation.
