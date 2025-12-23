import unittest

from teszteles.multiply_numbers import multiply

class TestMultiplyNumbers(unittest.TestCase):
    def test_multiply(self):
        test_cases = [
            (2, 3, 6),
            (0, 5, 0),
            (-1, 5, -5),
            (-2, -2, 4)
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(multiply(a, b), expected)

if __name__ == '__main__':
    unittest.main()
