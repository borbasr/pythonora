import unittest

from egysegtesztek.szamologep import add

class TestCalculation(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(a=2, b=3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, b=3), 1)

    def test_app_zero(self):
        self.assertEqual(add(a=0, b=5), 5)
        self.assertEqual(add(a=5, b=0), 5)

if __name__ == '__main__':
    unittest.main()
