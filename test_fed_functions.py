import unittest
import fed_functions as ff

class TestFedFunctions(unittest.TestCase):
    def test_type_get_interest_rate(self):
        # Tests the length and type of the output
        actual = type(ff.get_overnight_rate())
        expected = float
        self.assertEquals(actual, expected)
