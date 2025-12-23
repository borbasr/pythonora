import unittest

from teszteles.61_user_management import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()
        self.manager.add_user('Elek')
        self.manager.add_user('Jakab')

    def tearDown(self):
        self.manager = None

    def test_add_user(self):
        self.manager.add_user('Mari')
        self.assertIn('Mari', self.manager.get_users())

    def test_remove_user(self):
        self.manager.remove_users('Elek')
        self.assertNotIn('Elek', self.manager.get_users())

    def test_get_users(self):
        users = self.manager.get_users()
        self.assertEqual(users, ['Elek', 'Jakab'])

if __name__ == '__main__':
     unittest.main()


