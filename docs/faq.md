# Mom's Canning Timer — FAQ

## Does it need anything installed besides Python?

No. There are no third-party dependencies — tkinter is part of the standard library. On some
Linux distributions tkinter is packaged separately from Python, which is the one thing worth
checking.

## Nothing happens when I run it.

Almost always missing tkinter:

```bash
sudo apt install python3-tk       # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
```

See [Troubleshooting](./troubleshooting.md).

## Do I need Python at all?

Not on Windows — the
[latest release](https://github.com/willtheorangeguy/Moms-Canning-Timer/releases/latest)
includes a built executable.

## Can I run more than one timer at once?

Yes, that is the point. Four burners, each with its own independent state — different lengths,
started at different moments, paused independently.

## Are the timers accurate enough for canning?

They count down in a GUI event loop, so they are kitchen-timer accurate rather than
laboratory accurate. For processing times where a minute matters, treat it as you would any
kitchen timer and give yourself margin.

**Processing times come from your recipe or canning guide, not from this program.**

## What happens when a timer finishes?

A bell sounds and a popup appears. The popup has to be dismissed, so a finished timer is still
obvious if you were out of the room.

## Can I set seconds rather than minutes?

The input is minutes. See [Configuration](./configuration.md).

## Why are there three ways to start it?

`main.py` runs from a clone with nothing installed; `canning-timer` is the console script from
`pip install`; `python -m moms_canning_timer` is the module form. All three reach the same
program — the first exists so you can use it on a machine you would rather not install
packages onto.

## Does it save anything?

No. Timers are in-memory and reset when the window closes. There is no state file and nothing
to back up.

## Which branch is the default?

`master`, not `main`.
