"""Tests for the CircularTimer widget (require a Tk display)."""

import unittest

import tkinter as tk

from gui_support import DISPLAY_AVAILABLE
from moms_canning_timer.widget import CircularTimer


@unittest.skipUnless(DISPLAY_AVAILABLE, "no Tk display available")
class TestCircularTimer(unittest.TestCase):
    """Construction and control behaviour of a single timer widget.

    A single Tk root is shared across the class; each test builds a fresh
    widget on it. Creating one root per test leaks Tcl interpreters and is
    flaky on some platforms.
    """

    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()
        cls.root.withdraw()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def setUp(self):
        self.alerts = []
        self.widget = CircularTimer(
            self.root, number=1, minutes=1, alert=lambda: self.alerts.append(True)
        )

    def tearDown(self):
        self.widget.destroy()

    def test_initial_display(self):
        self.assertEqual(self.widget.state.display(), "01:00")

    def test_start_runs_timer(self):
        self.widget.start()
        self.assertTrue(self.widget.state.running)
        self.assertEqual(str(self.widget.pause_button["state"]), tk.NORMAL)

    def test_toggle_pause(self):
        self.widget.start()
        self.widget.toggle_pause()
        self.assertFalse(self.widget.state.running)
        self.assertEqual(self.widget.pause_button["text"], "Resume")
        self.widget.toggle_pause()
        self.assertTrue(self.widget.state.running)
        self.assertEqual(self.widget.pause_button["text"], "Pause")

    def test_reset(self):
        self.widget.start()
        self.widget.state.tick()
        self.widget.reset()
        self.assertEqual(
            self.widget.state.remaining_seconds, self.widget.state.total_seconds
        )
        self.assertFalse(self.widget.state.running)

    def test_finish_fires_alert(self):
        self.widget.start()
        # Drive to completion through the widget's own tick path.
        for _ in range(self.widget.state.total_seconds):
            self.widget._tick()  # pylint: disable=protected-access
        self.assertTrue(self.widget.state.finished)
        self.assertEqual(self.alerts, [True])

    def test_start_reads_spinbox(self):
        self.widget.minutes_var.set("3")
        self.widget.start()
        self.assertEqual(self.widget.state.total_seconds, 180)


if __name__ == "__main__":
    unittest.main()
