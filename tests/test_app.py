# assuming your function is in app.py
import unittest
import os
import sys
DIR = os.path.dirname(os.path.dirname(__file__))  # The repo root directory
sys.path.append(DIR)


class TestAdd2(unittest.TestCase):
    def test_add2_with_positive_number(self):
        self.assertEqual(add2(3), 5, "Should be 5")

    def test_add2_with_negative_number(self):
        self.assertEqual(add2(-3), -1, "Should be -1")

    def test_add2_with_zero(self):
        self.assertEqual(add2(0), 2, "Should be 2")


if __name__ == '__main__':
    from app import add2
    unittest.main()
