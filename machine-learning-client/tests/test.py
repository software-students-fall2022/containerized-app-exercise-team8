import pytest
import sys
from app import app


class Tests:

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Sanity test to return true
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_parse_phrase_from_voice_returntype(self):
        assert isinstance(app.parse_phrase_from_voice(
            "machine-learning-client/Sample-text-for-SWE.wav"), str), "did not return transcribed audio as string"

    def test_calculate_sentiment_returntype(self):
        assert isinstance(app.calculate_sentiment("hello, this is a test phrase"),
                          dict), "did not return dictionary with sentiment analysis"

    def test_check_new_user_returntype(self):
        assert isinstance(app.check_new_user("xyz123"),
                          bool), "did not return boolean value"
