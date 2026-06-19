"""Main window: a 2x2 grid of canning timers laid out like a stove."""

# Mom's Canning Timer - Customizable stove top timers.
# Copyright (C) 2017-2026 willtheorangeguy

import tkinter as tk

from .widget import CircularTimer

GRID_POSITIONS = ((0, 0), (0, 1), (1, 0), (1, 1))


def build_window():
    """Create the main window with four timers in a 2x2 stove grid.

    Returns the :class:`tkinter.Tk` instance without starting the event loop,
    so callers (and tests) can inspect or drive it.
    """
    window = tk.Tk()
    window.title("Canning Timer")

    timers = []
    for index, (row, column) in enumerate(GRID_POSITIONS, start=1):
        timer = CircularTimer(window, number=index)
        timer.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")
        timers.append(timer)

    for row in range(2):
        window.grid_rowconfigure(row, weight=1)
    for column in range(2):
        window.grid_columnconfigure(column, weight=1)

    window.timers = timers
    return window


def main():
    """Console-script entry point: build the window and run the event loop."""
    build_window().mainloop()


if __name__ == "__main__":
    main()
