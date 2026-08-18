<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Moms-Canning-Timer/logo.png" height="350px" width="400px" alt="Mom's Canning Timer">
  <br>
  Mom's Canning Timer
  <br>
</h1>

<!-- Copy -->
<h4 align="center">Four stove-top timers in a 2x2 grid, built for preserving fruit and vegetables for the winter.</h4>

<!-- Badges -->
<div align="center">
  <img alt="PyPI Build State" src="https://github.com/willtheorangeguy/Moms-Canning-Timer/actions/workflows/push-to-pypi.yml/badge.svg">
  <img alt="Pytest State" src="https://github.com/willtheorangeguy/Moms-Canning-Timer/actions/workflows/pytest.yml/badge.svg">
  <img alt="Pylint State" src="https://github.com/willtheorangeguy/Moms-Canning-Timer/actions/workflows/pylint.yml/badge.svg">
  <img alt="CodeQL State" src="https://github.com/willtheorangeguy/Moms-Canning-Timer/actions/workflows/codeql-analysis.yml/badge.svg">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Moms-Canning-Timer?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Moms-Canning-Timer">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Moms-Canning-Timer">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Hero -->
<div align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Moms-Canning-Timer/welcome.png" alt="Mom's Canning Timer">
</div>

## Key Features

- Four timers in a 2x2 grid, laid out like a stove top.
- A circular progress ring around each one.
- Set each timer's length in minutes, in the GUI.
- Start, pause, resume, and reset per burner, independently.
- A bell and a popup when a timer finishes.
- Cross-platform, with **no third-party dependencies** — pure standard-library tkinter.

## Installation

```bash
pip install moms-canning-timer
canning-timer
```

Requires Python. See [`docs/installation.md`](docs/installation.md) for running from source or the Windows executable.

## Usage

Set a length on each burner you need, press start, and the ring fills as it counts down. Each timer runs independently.

## Documentation

Full documentation lives in [`docs/`](docs/README.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Usage](docs/usage.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [Testing](docs/testing.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/Moms-Canning-Timer/discussions/new) or file an [issue](https://github.com/willtheorangeguy/Moms-Canning-Timer/issues/new/choose).

## Contributing

Contributions welcome. See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

Built with [Python](https://www.python.org/) and its standard-library tkinter. Published to the [Python Package Index](https://pypi.org/project/Moms-Canning-Timer/).

## License

MIT — see [`LICENSE.md`](LICENSE.md).

> A kitchen timer, not a food-safety authority. Processing times come from your recipe or your canning guide, not from this program.
