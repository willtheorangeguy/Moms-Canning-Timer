"""Tests for __main__.py."""

# pylint: disable=invalid-name

import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestEntrypoint(unittest.TestCase):
    """Tests for __main__.py."""

    def test_main_module_exists(self):
        """Test that __main__.py file exists."""
        main_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__main__.py"
        )
        self.assertTrue(os.path.exists(main_path))

    def test_main_has_correct_imports(self):
        """Test that __main__.py has the correct structure."""
        main_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__main__.py"
        )
        with open(main_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("from main import timer", content)
            self.assertIn('if __name__ == "__main__":', content)

    def test_main_has_docstring(self):
        """Test that __main__.py has a docstring."""
        main_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "__main__.py"
        )
        with open(main_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Check for docstring at the beginning
            self.assertIn('"""', content)


if __name__ == "__main__":
    unittest.main()
