import unittest
from unittest.mock import MagicMock

from teszteles.auth_services import AuthService

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth = AuthService()

    def test_login_success(self):
        self.auth.login = MagicMock(return_value='MOCK_TOKEN')
        token = self.auth.login('elek', 'alma')
        self.assertEqual(token, 'MOCK_TOKEN')

    def test_login_failure(self):
        self.auth.login = MagicMock(side_effect=ValueError('Hiba!'))
        with self.assertRaises(ValueError):
            self.auth.login('aaa', 'vvv')

    if __name__ == '__main__':
        unittest.main()


