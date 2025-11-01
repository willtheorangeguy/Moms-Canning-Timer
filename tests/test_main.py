"""Tests for main.py."""

# pylint: disable=invalid-name, wrong-import-position

import sys
import os
import unittest
from unittest.mock import patch, MagicMock
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import timeStart1, timeStart2, timeStart3, timeStart4, timer


class TestTimer(unittest.TestCase):
    """Tests for timer.py."""

    def test_timeStart1_callable(self):
        """Test timeStart1 function is callable."""
        self.assertTrue(callable(timeStart1))

    def test_timeStart2_callable(self):
        """Test timeStart2 function is callable."""
        self.assertTrue(callable(timeStart2))

    def test_timeStart3_callable(self):
        """Test timeStart3 function is callable."""
        self.assertTrue(callable(timeStart3))

    def test_timeStart4_callable(self):
        """Test timeStart4 function is callable."""
        self.assertTrue(callable(timeStart4))

    @patch("time.sleep")
    @patch("builtins.print")
    def test_timeStart1_execution(self, mock_print, mock_sleep):
        """Test timeStart1 runs without errors when mocked."""

        # Run in a thread with timeout to prevent hanging
        def run_timer():
            timeStart1()

        thread = threading.Thread(target=run_timer)
        thread.daemon = True
        thread.start()
        thread.join(timeout=2.0)

        # Verify that print was called (timer is running)
        self.assertTrue(mock_print.called)
        # Verify that sleep was called (timer is working)
        self.assertTrue(mock_sleep.called)

    @patch("time.sleep")
    @patch("builtins.print")
    def test_timeStart2_execution(self, mock_print, mock_sleep):
        """Test timeStart2 runs without errors when mocked."""

        def run_timer():
            timeStart2()

        thread = threading.Thread(target=run_timer)
        thread.daemon = True
        thread.start()
        thread.join(timeout=2.0)

        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)

    @patch("time.sleep")
    @patch("builtins.print")
    def test_timeStart3_execution(self, mock_print, mock_sleep):
        """Test timeStart3 runs without errors when mocked."""

        def run_timer():
            timeStart3()

        thread = threading.Thread(target=run_timer)
        thread.daemon = True
        thread.start()
        thread.join(timeout=2.0)

        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)

    @patch("time.sleep")
    @patch("builtins.print")
    def test_timeStart4_execution(self, mock_print, mock_sleep):
        """Test timeStart4 runs without errors when mocked."""

        def run_timer():
            timeStart4()

        thread = threading.Thread(target=run_timer)
        thread.daemon = True
        thread.start()
        thread.join(timeout=2.0)

        self.assertTrue(mock_print.called)
        self.assertTrue(mock_sleep.called)

    def test_timer_callable(self):
        """Test timer function is callable."""
        self.assertTrue(callable(timer))

    @patch("main.Tk")
    def test_timer_creates_window(self, mock_tk):
        """Test timer function creates a Tk window."""
        # Mock the Tk instance and its methods
        mock_window = MagicMock()
        mock_tk.return_value = mock_window

        # Run timer in a thread to avoid blocking
        def run_timer():
            try:
                timer()
            except:
                pass  # Expected to fail when mainloop is not properly mocked

        thread = threading.Thread(target=run_timer)
        thread.daemon = True
        thread.start()
        thread.join(timeout=1.0)

        # Verify Tk was instantiated
        mock_tk.assert_called_once()
        # Verify window title was set
        mock_window.title.assert_called_once_with("Canning Timer")


if __name__ == "__main__":
    unittest.main()
