import pytest
from unittest.mock import patch
from culinary.culinary_api.culinary_api import search_recipe


def test_mock_search_recipes():
    with patch('culinary.culinary_api.culinary_api.requests.get') as mock_get:
        # Mock out the response from the Spoonacular API
        mock_response = {
            'results': [
                {'title': 'Mock Recipe 1'},
                {'title': 'Mock Recipe 2'},
            ]
        }
        mock_get.return_value.json.return_value = mock_response

        # Call the function you're testing
        results = search_recipe('mock query')

        # Assert that the function returned the expected results
        assert results == mock_response['results']