"""Pure countdown logic for a single canning timer.

This module is deliberately free of any tkinter dependency so the timer
behaviour can be unit tested without a display.
"""

# Mom's Canning Timer - Customizable stove top timers.
# Copyright (C) 2017-2026 willtheorangeguy

MIN_MINUTES = 1
MAX_MINUTES = 180
SECONDS_PER_MINUTE = 60


class TimerState:
    """Tracks the countdown state for one burner.

    A timer is configured with a duration in minutes, then started. Each call
    to :meth:`tick` advances the countdown by one second. The state never
    touches the GUI; the widget reads it to render the progress ring.
    """

    def __init__(self, minutes=15):
        self.total_seconds = 0
        self.remaining_seconds = 0
        self.running = False
        self.finished = False
        self.set_minutes(minutes)

    def set_minutes(self, minutes):
        """Configure the timer duration in minutes and reset its progress.

        The value is clamped to ``[MIN_MINUTES, MAX_MINUTES]``.
        """
        minutes = int(minutes)
        minutes = max(MIN_MINUTES, min(MAX_MINUTES, minutes))
        self.total_seconds = minutes * SECONDS_PER_MINUTE
        self.remaining_seconds = self.total_seconds
        self.running = False
        self.finished = False

    def start(self):
        """Start (or restart) the countdown from its full duration."""
        self.remaining_seconds = self.total_seconds
        self.finished = False
        self.running = self.total_seconds > 0

    def pause(self):
        """Pause a running countdown. No effect if not running."""
        self.running = False

    def resume(self):
        """Resume a paused countdown if time remains."""
        if not self.finished and self.remaining_seconds > 0:
            self.running = True

    def reset(self):
        """Stop the timer and restore the remaining time to the full duration."""
        self.remaining_seconds = self.total_seconds
        self.running = False
        self.finished = False

    def tick(self):
        """Advance the countdown by one second.

        Returns ``True`` only on the tick that drives the timer to zero, so the
        caller can fire a one-shot "done" alert.
        """
        if not self.running:
            return False
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        if self.remaining_seconds <= 0:
            self.remaining_seconds = 0
            self.running = False
            self.finished = True
            return True
        return False

    def fraction_done(self):
        """Return progress as a float in ``[0.0, 1.0]`` for the ring sweep."""
        if self.total_seconds <= 0:
            return 0.0
        elapsed = self.total_seconds - self.remaining_seconds
        return elapsed / self.total_seconds

    def display(self):
        """Return the remaining time formatted as ``MM:SS``."""
        minutes, seconds = divmod(self.remaining_seconds, SECONDS_PER_MINUTE)
        return f"{minutes:02d}:{seconds:02d}"
