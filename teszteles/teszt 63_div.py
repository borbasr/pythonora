import unittest

from teszteles.63_div import divide

class TestDiv(unittest.TestCase):

    def test_divide_valid(self):
        self.assertEqual(divide(a: 10, b: 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(a: 10, b: 0)
        self.assertEqual(str(context.exception, 'B szam nem lehet 0!'))

if __name__ == '__main__':
    unittest.main()
