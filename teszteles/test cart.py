import unittest

from teszteles.cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_item('alma', 3)
        self.cart.add_item('banan', 2)

    def test_add_tem(self):
        self.cart.add_item('narancs', 5)
        self.assertEqual(self.cart.items['narancs'], 5)

    def remove_item(self):
        self.cart.remove_item('alma')
        self.assertNotIn('alma', self.cart.items)

    def test_sum_items(self):
        total = self.cart.get_total_items()
        self.assertEqual(total, 5)

if __name__ == '__main__':
    unittest.main()

