"""Tests for __init__.py."""

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import __init__


class TestInit(unittest.TestCase):
    """Tests for __init__.py."""

    def test_all_attribute_exists(self):
        """Test that __all__ attribute exists."""
        self.assertTrue(hasattr(__init__, "__all__"))

    def test_all_contains_main(self):
        """Test that __all__ contains 'main'."""
        self.assertIn("main", __init__.__all__)

    def test_all_is_list(self):
        """Test that __all__ is a list."""
        self.assertIsInstance(__init__.__all__, list)


if __name__ == "__main__":
    unittest.main()
