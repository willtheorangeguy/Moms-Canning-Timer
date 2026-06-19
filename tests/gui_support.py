"""Shared helper for GUI tests: detect whether a Tk display is available."""

import tkinter as tk


def display_available():
    """Return True if a Tk root can be created (a display/X server exists)."""
    try:
        root = tk.Tk()
    except tk.TclError:
        return False
    root.destroy()
    return True


DISPLAY_AVAILABLE = display_available()
