from django.test import TestCase
from django.http import HttpRequest
from unittest.mock import patch
from Quiz.views import get_data

class GetDataTestCase(TestCase):
    @patch('Quiz.views.requests.get')
    def test_get_data_success(self, mock_get):

        expected_response = [
            {
                'category': 'Geography',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'A group of islands is called an &#039;archipelago&#039;.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Geography',
                'type': 'multiple',
                'difficulty': 'easy',
                'question': 'All of the following are classified as Finno-Ugric languages EXCEPT:',
                'correct_answer': 'Samoyedic',
                'incorrect_answers': ['Hungarian', 'Finnish', 'Estonian']
            },
            
        ]
        # Mock the response from the external API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        # Create a mock request object
        request = HttpRequest()

        # Call the view function
        response = get_data(request)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), expected_response)
            

    @patch('Quiz.views.requests.get')
    def test_get_data_failure(self, mock_get):
        # Mock the response from the external API
        mock_get.return_value.status_code = 404

        # Create a mock request object
        request = HttpRequest()

        # Call the view function
        response = get_data(request)

        # Assert the response status code
        self.assertEqual(response.status_code, 404)