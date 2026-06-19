"""The :class:`CircularTimer` widget: one burner with a circular progress ring."""

# Mom's Canning Timer - Customizable stove top timers.
# Copyright (C) 2017-2026 willtheorangeguy

import tkinter as tk
from tkinter import messagebox

from .state import MAX_MINUTES, MIN_MINUTES, TimerState

CANVAS_SIZE = 160
RING_PADDING = 18
RING_WIDTH = 12
TICK_MS = 1000

TRACK_COLOR = "#e0e0e0"
PROGRESS_COLOR = "#2e8b57"
DONE_COLOR = "#c0392b"
TEXT_COLOR = "#222222"

# Arcs are measured counter-clockwise from 3 o'clock; start at the top.
ARC_START = 90


class CircularTimer(tk.Frame):
    """A single canning timer rendered as a ring of progress with controls.

    The countdown is driven by :meth:`tkinter.Misc.after` so the GUI event loop
    is never blocked. ``alert`` is injectable so tests can run the finish path
    without popping a real dialog.
    """

    def __init__(self, master, number, minutes=15, alert=None, **kwargs):
        super().__init__(master, **kwargs)
        self.number = number
        self.state = TimerState(minutes)
        self._alert = alert if alert is not None else self._default_alert
        self._after_id = None

        title = tk.Label(self, text=f"Burner #{number}", font=("Helvetica", 12, "bold"))
        title.pack(pady=(4, 2))

        self.canvas = tk.Canvas(
            self,
            width=CANVAS_SIZE,
            height=CANVAS_SIZE,
            highlightthickness=0,
        )
        self.canvas.pack()

        box = (
            RING_PADDING,
            RING_PADDING,
            CANVAS_SIZE - RING_PADDING,
            CANVAS_SIZE - RING_PADDING,
        )
        self.canvas.create_oval(*box, outline=TRACK_COLOR, width=RING_WIDTH)
        self._arc = self.canvas.create_arc(
            *box,
            start=ARC_START,
            extent=0,
            style=tk.ARC,
            outline=PROGRESS_COLOR,
            width=RING_WIDTH,
        )
        self._text = self.canvas.create_text(
            CANVAS_SIZE / 2,
            CANVAS_SIZE / 2,
            text=self.state.display(),
            font=("Helvetica", 22, "bold"),
            fill=TEXT_COLOR,
        )

        controls = tk.Frame(self)
        controls.pack(pady=4)

        tk.Label(controls, text="Min:").grid(row=0, column=0, padx=2)
        self.minutes_var = tk.StringVar(value=str(minutes))
        self.spinbox = tk.Spinbox(
            controls,
            from_=MIN_MINUTES,
            to=MAX_MINUTES,
            width=4,
            textvariable=self.minutes_var,
        )
        self.spinbox.grid(row=0, column=1, padx=2)

        self.start_button = tk.Button(controls, text="Start", command=self.start)
        self.start_button.grid(row=0, column=2, padx=2)

        self.pause_button = tk.Button(
            controls, text="Pause", command=self.toggle_pause, state=tk.DISABLED
        )
        self.pause_button.grid(row=1, column=0, columnspan=2, pady=2, sticky="ew")

        self.reset_button = tk.Button(controls, text="Reset", command=self.reset)
        self.reset_button.grid(row=1, column=2, pady=2, sticky="ew")

        self._redraw()

    def _default_alert(self):
        """Ring the bell and show the done dialog."""
        self.bell()
        messagebox.showinfo("Canning Timer", f"Burner #{self.number} is done!")

    def start(self):
        """Read the spinbox duration and begin the countdown."""
        try:
            minutes = int(self.minutes_var.get())
        except (TypeError, ValueError):
            minutes = MIN_MINUTES
        self.state.set_minutes(minutes)
        self.minutes_var.set(str(self.state.total_seconds // 60))
        self.state.start()
        self.pause_button.config(text="Pause", state=tk.NORMAL)
        self._redraw()
        self._schedule()

    def toggle_pause(self):
        """Pause a running timer or resume a paused one."""
        if self.state.running:
            self.state.pause()
            self.pause_button.config(text="Resume")
            self._cancel()
        else:
            self.state.resume()
            if self.state.running:
                self.pause_button.config(text="Pause")
                self._schedule()
        self._redraw()

    def reset(self):
        """Stop the timer and restore the full duration."""
        self._cancel()
        self.state.reset()
        self.pause_button.config(text="Pause", state=tk.DISABLED)
        self._redraw()

    def _schedule(self):
        """Queue the next one-second tick."""
        self._cancel()
        self._after_id = self.after(TICK_MS, self._tick)

    def _cancel(self):
        """Cancel any pending tick callback."""
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self._after_id = None

    def _tick(self):
        """Advance one second, redraw, and fire the alert on completion."""
        self._after_id = None
        just_finished = self.state.tick()
        self._redraw()
        if just_finished:
            self.pause_button.config(state=tk.DISABLED)
            self._alert()
        elif self.state.running:
            self._schedule()

    def _redraw(self):
        """Sync the ring sweep and centered text to the current state."""
        extent = -self.state.fraction_done() * 360
        color = DONE_COLOR if self.state.finished else PROGRESS_COLOR
        self.canvas.itemconfigure(self._arc, extent=extent, outline=color)
        self.canvas.itemconfigure(self._text, text=self.state.display())
