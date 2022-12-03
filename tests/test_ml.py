import pytest
import sys
sys.path.append('machine_learning_client')
from app import app
from speech_analysis import speech_analysis

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
    
    def test_index_returntype(self):
        """
        Verify that index() returns an html template
        """
        actual = app.index()
        assert isinstance(actual, str), f"Expected index() to return a string, instead it returned {actual}"
        assert len(actual) > 0, f"Expected index() not to be empty. Instead, it returned an empty string"

    def test_upload_retyruntype(self):
        """
        Verify that upload() returns an html template
        """
        actual = app.upload()
        assert isinstance(actual, str), f"Expected upload() to return a string, instead it returned {actual}"
        assert len(actual) > 0, f"Expected upload() not to be empty. Instead, it returned an empty string"

    def test_calculate_sentiment_returntype(self):
        """
        Verify that calculate_sentiment() returns a decimal
        """
        actual = app.calculate_sentiment("hey there! testing some code hehe")
        assert isinstance(actual, float), f"Expected calculate_sentiment() to return a decimal, instead it returned {actual}"
        assert len(actual) > 0, f"Expected upload() not to be empty. Instead, it returned empty"

    def test_parse_phrase_from_voice_returntype(self):
        assert isinstance(app.parse_phrase_from_voice("machine-learning-client/Sample-text-for-SWE.wav"), str), "did not return transcribed audio as string"

    def test_calculate_sentiment_returntype(self):
        assert isinstance(app.calculate_sentiment("hello, this is a test phrase"), dict), "did not return dictionary with sentiment analysis"

    def test_check_new_user_returntype(self):
        assert isinstance(app.check_new_user("xyz123"), bool), "did not return boolean value"

    def test_speech_analysis_get_sentiment_returntype(self):
        actual = speech_analysis.get_sentiment('hey there! testing hehe')
        assert isinstance(actual, float), f'Expected get_sentiment() to return a float, instead it returned {actual}'