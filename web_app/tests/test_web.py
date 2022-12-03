import pytest
from app import app

class Tests:
    #
    # Test functions
    #
    def test_sentiment_guesser(self):
        """
        Verify that index() returns an html template
        """
        actual = app.sentiment_guesser()
        assert isinstance(actual, str), f"Expected sentiment_guesser() to return a string, instead it returned {actual}"
        assert len(actual) > 0, f"Expected sentiment_guesser() not to be empty. Instead, it returned an empty string"