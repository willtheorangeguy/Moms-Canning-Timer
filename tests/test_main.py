"""Tests for main.py."""
# pylint: disable=invalid-name, wrong-import-position

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import timeStart1, timeStart2, timeStart3, timeStart4


class TestTimer(unittest.TestCase):
    """Tests for timer.py."""

    def test_timeStart1(self):
        """Test timeStart1 function."""
        self.assertTrue(callable(timeStart1))

    def test_timeStart2(self):
        """Test timeStart2 function."""
        self.assertTrue(callable(timeStart2))

    def test_timeStart3(self):
        """Test timeStart3 function."""
        self.assertTrue(callable(timeStart3))

    def test_timeStart4(self):
        """Test timeStart4 function."""
        self.assertTrue(callable(timeStart4))


if __name__ == "__main__":
    unittest.main()
