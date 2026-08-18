# Mom's Canning Timer — Troubleshooting

## No window opens

The most common problem, and almost always missing tkinter. It ships with Python on Windows
and macOS, but several Linux distributions package it separately:

```bash
sudo apt install python3-tk       # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
sudo pacman -S tk                 # Arch
```

Confirm it directly:

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

An `ImportError` there is the whole explanation.

## `canning-timer: command not found`

The console script did not land on your `PATH` — usually a virtual environment that is not
active, or a user-level bin directory that is not on `PATH`.

Both of these work regardless:

```bash
python -m moms_canning_timer
python main.py
```

## Running over SSH does nothing

It is a desktop application and needs a display. Over SSH you need X forwarding, or to run it
on the machine itself.

## No bell when a timer finishes

The popup should still appear. Terminal bell behaviour varies by platform and terminal, and
some desktop environments suppress it — the visual alert is the reliable half.

## A timer drifts by a few seconds

Expected. The countdown runs in the GUI event loop, so it is kitchen-timer accurate rather
than exact. Give yourself margin on processing times that matter.

## Timers reset when I close the window

Nothing is saved — timer state is in memory only. Closing the window clears everything.

## Pausing one timer affected another

It should not. Each burner has its own state object, so they are independent. If you see this,
it is worth reporting with the steps.

## `pip install -e .` fails

Check you are in the repository root, where `pyproject.toml` sits. If you would rather not
install at all, `python main.py` runs the program straight from the folder.

## Tests fail with a display error

`tests/gui_support.py` exists so widget tests can run without a real display. If you see
display errors, run the state tests alone to confirm the logic is fine:

```bash
pytest tests/test_state.py
```

See [Testing](./testing.md).
