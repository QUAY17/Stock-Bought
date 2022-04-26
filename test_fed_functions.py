import unittest
import fed_functions as ff
import fredpy as fp

class TestFedFunctions(unittest.TestCase):

    # API key to access DB
    ff.load_api_key()

    # for the 10yr interest rate:
    def test_type_get_interest_rate(self):
        # Tests the type of the output
        actual = type(ff.get_interest_rate().tolist())
        expected = float
        self.assertEqual(actual, expected)

    def test_length_get_interest_rate(self):
        # Tests the length and type of the output
        responses = []
        responses.append(ff.get_interest_rate())
        actual = len(responses)
        expected = 1
        self.assertEqual(actual, expected)

    # for the overnight interest rate:
    def test_type_get_overnight_rate(self):
        # Tests the type of the output
        actual = type(ff.get_overnight_rate().tolist())
        expected = float
        self.assertEqual(actual, expected)

    def test_length_get_overnight_rate(self):
        # Tests the length and type of the output
        responses = []
        responses.append(ff.get_overnight_rate())
        actual = len(responses)
        expected = 1
        self.assertEqual(actual, expected)
