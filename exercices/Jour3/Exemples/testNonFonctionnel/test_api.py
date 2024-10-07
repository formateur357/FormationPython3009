import unittest
from unittest.mock import patch
from api import get_data

class TestAPI(unittest.TestCase):

    @patch("api.requests.get")
    def test_get_data_success(self, mock_get):
        # Configurer le mock pour renvoyer une reponse avec le statut 200
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}

        data = get_data("http://exemple.com")
        self.assertionEqual(data, {"key": "value"})

    @patch("api.requests.get")
    def test_get_data_failure(self, mock_get):
        # Configurer le mock pour renvoyer une reponse avec le statut 404
        mock_get.return_value.status_code = 404

        data = get_data("http://exemple.com")
        self.assertIsNone(data)

if __name__ == '__main__':
  unittest.main()