# Mom's Canning Timer — Architecture

## Layout

```
main.py                          run from a clone, no install
src/moms_canning_timer/
├── __main__.py                  python -m moms_canning_timer
├── app.py                       the window and the 2x2 grid
├── widget.py                    one burner: ring, entry, buttons
└── state.py                     timer state, with no GUI knowledge
```

Packaged with a `src/` layout and published to PyPI as `moms-canning-timer`, with a
`canning-timer` console script.

## State is separate from the widget

`state.py` holds the countdown logic — duration, elapsed, running, paused — and knows nothing
about tkinter. `widget.py` renders one burner and drives that state.

That split is what makes the timers testable. `tests/test_state.py` exercises the logic
directly with no display at all, which is why the suite can run in CI where no window can be
opened.

It also means the four burners are genuinely independent: each has its own state object, so
pausing one has no effect on the others.

## No third-party dependencies

`requirements.txt` pulls in nothing at runtime. tkinter is standard library.

That is a deliberate constraint rather than an accident of a small program. It means the app
installs on a machine with no compiler and no network, starts instantly, and cannot be broken
by a dependency update — appropriate for something opened in a kitchen while jars are
boiling.

Adding a dependency should be weighed against losing that.

## Three ways in, one program

| Entry point | For |
|---|---|
| `main.py` | Running from a clone with nothing installed |
| `canning-timer` | The console script from `pip install` |
| `python -m moms_canning_timer` | The module form |

All three reach the same application.

## The finish alert

A bell plus a popup. The popup requires dismissal, which is the point — a timer that finishes
while you are across the room should still be obvious when you come back.

## Testing

`tests/gui_support.py` provides the scaffolding that lets widget tests run without a real
display. See [Testing](./testing.md).

## CI

Four workflows: pytest, pylint, CodeQL analysis, and publish-to-PyPI on release.
