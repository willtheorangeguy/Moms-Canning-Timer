# Mom's Canning Timer — Installation

## Requirements

Python, with tkinter. That is the whole list — there are **no third-party dependencies**.

tkinter ships with Python on Windows and macOS. Some Linux distributions package it
separately:

```bash
sudo apt install python3-tk       # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
```

## From PyPI

```bash
pip install moms-canning-timer
canning-timer
```

## From source

```bash
git clone https://github.com/willtheorangeguy/Moms-Canning-Timer
cd Moms-Canning-Timer
```

Then either run it directly:

```bash
python main.py
```

or install it so the command and module entry points work:

```bash
pip install -e .
canning-timer
python -m moms_canning_timer
```

`main.py` exists so you can run the program from a clone with no install step at all — useful
on a machine you would rather not install packages onto.

## Windows executable

The [latest release](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/latest)
includes a built executable for Windows. **It does not require Python.**

## Verify

```bash
canning-timer
```

A window with four timers should open. If nothing appears, tkinter is the usual cause — see
[Troubleshooting](./troubleshooting.md).

## Next

[Quickstart](./quickstart.md), or [Usage](./usage.md).
