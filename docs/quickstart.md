# Mom's Canning Timer — Quickstart

## 1. Install

```bash
pip install moms-canning-timer
```

Nothing else is needed — no compiler, no third-party packages. tkinter comes with Python.

## 2. Run it

```bash
canning-timer
```

Equivalent alternatives:

```bash
python -m moms_canning_timer
python main.py            # from a clone, without installing
```

## 3. Use a burner

The window shows four timers in a 2x2 grid, like a stove top.

For each one:

1. Type a length in **minutes**.
2. Press **Start**.
3. The ring around the timer fills as it counts down.
4. **Pause** and **Resume** as needed; **Reset** clears it.

Each burner is independent — four different jars, four different times, all running at once.

## 4. When it finishes

A bell sounds and a popup appears. The popup needs dismissing, so a finished timer stays
noticeable if you have walked away.

## If nothing opens

Almost always missing tkinter, which some Linux distributions package separately from Python:

```bash
sudo apt install python3-tk      # Debian/Ubuntu
```

See [Troubleshooting](./troubleshooting.md).

## Then what

- [Usage](./usage.md) — the controls in detail
- [Installation](./installation.md) — running from source, or the Windows executable
