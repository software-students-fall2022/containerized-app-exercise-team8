import pytest
import sys


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
