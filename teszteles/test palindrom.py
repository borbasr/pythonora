import unittest

from teszteles.palindrom import is_palindrom


class TestPalindrom(unittest.TestCase):
    def test_paliindrom_true(self):
        self.assertTrue(is_palindrom('legeL'))

    def test_paliindrom_false(self):
        self.assertFalse(is_palindrom('valami'))


if __name__ == '__main__':
    unittest.main()
