from django.test import TestCase, Client
from unittest.mock import patch
from Quiz.views import get_data

class GetDataTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('quiz.views.requests.get')
    def test_get_data_success(self, mock_get):
        # Mock the API call to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'key': 'value'}

        response = self.client.get('/your-url-path/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'key': 'value'})

    @patch('quiz.views.requests.get')
    def test_get_data_failure(self, mock_get):
        # Mock the API call to return a failure response
        mock_get.return_value.status_code = 404

        response = self.client.get('/your-url-path/')
        self.assertEqual(response.status_code, 404)