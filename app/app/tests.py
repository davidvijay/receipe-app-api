"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""
    def test_add_numbers(self):
        """Testing adding numbers together."""
        res= calc.add(5, 6)
        self.assertEqual(res, 11)
    def test_subtract_numbers(self):
        """Testing numbers with subrtaction"""
        res = calc.subrtaction(5, 6)
        self.assertEqual(res, 1)
