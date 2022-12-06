import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

app.app_context()

class Tests:
    #
    # Test functions
    #
    def test_sanity_check(self):
        """
        Sanity test to return true
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_sentiment_guesser_returntype(self):
        """
        Verify that index() returns an html template
        """
        actual = app.sentiment_guesser()
        assert isinstance(actual, str), f"Expected sentiment_guesser() to return a string, instead it returned {actual}"
        assert len(actual) > 0, f"Expected sentiment_guesser() not to be empty. Instead, it returned an empty string"

    # test route "/" with GET
    def test_route(self):
        url = '/'
        response = app.get(url)
        assert response.status_code == 200, f"expected code 200"

    # test a fake route
    def test_fake_route(self):
        url = '/fakeRoute'
        response = app.get(url)
        assert response.status_code == 404, f"expected code 404"
