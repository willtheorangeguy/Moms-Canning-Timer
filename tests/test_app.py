"""Tests for the main window layout (require a Tk display)."""

import unittest

from gui_support import DISPLAY_AVAILABLE
from moms_canning_timer.app import GRID_POSITIONS, build_window
from moms_canning_timer.widget import CircularTimer


@unittest.skipUnless(DISPLAY_AVAILABLE, "no Tk display available")
class TestBuildWindow(unittest.TestCase):
    """The stove window holds four timers in a 2x2 grid.

    The window is read-only inspected, so a single instance is shared across the
    class rather than recreating a Tk root per test.
    """

    @classmethod
    def setUpClass(cls):
        cls.window = build_window()
        cls.window.withdraw()

    @classmethod
    def tearDownClass(cls):
        cls.window.destroy()

    def test_title(self):
        self.assertEqual(self.window.title(), "Canning Timer")

    def test_four_timers(self):
        self.assertEqual(len(self.window.timers), 4)
        for timer in self.window.timers:
            self.assertIsInstance(timer, CircularTimer)

    def test_two_by_two_grid(self):
        coords = set()
        for timer in self.window.timers:
            info = timer.grid_info()
            coords.add((int(info["row"]), int(info["column"])))
        self.assertEqual(coords, set(GRID_POSITIONS))
        self.assertEqual(coords, {(0, 0), (0, 1), (1, 0), (1, 1)})

    def test_burner_numbers(self):
        numbers = sorted(timer.number for timer in self.window.timers)
        self.assertEqual(numbers, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
