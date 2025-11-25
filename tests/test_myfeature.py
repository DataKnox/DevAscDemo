import os
import sys
import unittest

# When this test is executed directly (``python tests/test_myfeature.py``),
# the script directory becomes sys.path[0] which is ``.../tests``. That
# prevents importing the top-level `Feature` package. Add the project root
# to `sys.path` so `from Feature.myfeature import greet` works when run as a
# script and also under test discovery.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Feature.myfeature import greet


class TestGreet(unittest.TestCase):
    def test_greet_standard(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_strips_whitespace(self):
        self.assertEqual(greet("  Bob  "), "Hello, Bob!")

    def test_greet_empty_raises(self):
        with self.assertRaises(ValueError):
            greet("   ")

    def test_greet_non_str_raises(self):
        with self.assertRaises(TypeError):
            greet(None)  # type: ignore


if __name__ == "__main__":
    unittest.main()
