# Mom's Canning Timer — Documentation

Four independent countdown timers in a tkinter window, arranged like a stove top. No
third-party dependencies — the whole thing runs on the Python standard library.

```text
Moms-Canning-Timer/
├── docs/
│   ├── README.md          this page
│   ├── quickstart.md      install and start a timer
│   ├── installation.md    pip, source, or the Windows executable
│   ├── usage.md           running the timers
│   ├── configuration.md   changing defaults
│   ├── architecture.md    how state, widget, and app fit together
│   ├── development.md     working on it
│   ├── testing.md         the test suite, including GUI tests
│   ├── faq.md             dependencies, platforms, accuracy
│   ├── troubleshooting.md no window, no sound, tkinter missing
│   └── roadmap.md         known gaps and non-goals
├── main.py                run straight from the folder
└── src/moms_canning_timer/
    ├── app.py             the application window
    ├── state.py           timer state, independent of any widget
    ├── widget.py          one burner
    └── __main__.py        python -m moms_canning_timer
```

## Pages

- [Quickstart](./quickstart.md) — install and start your first timer
- [Installation](./installation.md) — PyPI, source, and the Windows build
- [Usage](./usage.md) — the four burners and their controls
- [Configuration](./configuration.md) — what can be changed
- [Architecture](./architecture.md) — why state is separate from the widget
- [Development](./development.md) — layout, linting, CI
- [Testing](./testing.md) — running the suite, including the GUI tests
- [FAQ](./faq.md) — dependencies, platforms, timer accuracy
- [Troubleshooting](./troubleshooting.md) — missing tkinter, no bell, no window
- [Roadmap](./roadmap.md) — known gaps and non-goals

## No dependencies is the point

`requirements.txt` pulls in nothing at runtime. tkinter ships with Python, so this installs
and runs on a machine with no build tools, no compiler, and no network — which is exactly
what you want from something opened in a kitchen while jars are boiling.
