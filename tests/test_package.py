"""Tests for package metadata and the console-script entry point."""

import unittest

import moms_canning_timer


class TestPackage(unittest.TestCase):
    """Public surface of the moms_canning_timer package."""

    def test_version(self):
        self.assertTrue(hasattr(moms_canning_timer, "__version__"))
        self.assertEqual(moms_canning_timer.__version__, "1.0.0")

    def test_all_exports(self):
        for name in ("main", "build_window", "CircularTimer", "TimerState"):
            self.assertIn(name, moms_canning_timer.__all__)
            self.assertTrue(hasattr(moms_canning_timer, name))

    def test_entry_point_callable(self):
        from moms_canning_timer.app import main  # pylint: disable=import-outside-toplevel

        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()
