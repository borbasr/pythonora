import unittest
from unittest.mock import patch

from teszteles.mock1 import get_data

class TestMock1(unittest.TestCase):

    @patch('mock1.requests.get')
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'alma': 20}

        result = get_data('valami')
        self.assertEqual(result, {'alma': 20})

        @patch('mock1.requests.get')
        def test_get_data_failure(self, mock_get):
            mock_get.return_value.status_code = 404

            with self.assertRaises(ValueError):
                get_data('Alma')

    if __name__ == '__main__':
        unittest.main()

