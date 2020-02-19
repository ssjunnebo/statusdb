import unittest
import mock
from StringIO import StringIO
from statusdb.tools.misc import query_yes_no, merge

class TestMisc(unittest.TestCase):
    def test_query_yes_no_force(self):
        response = query_yes_no("some question", force=True)
        self.assertTrue(response)

    @mock.patch('statusdb.tools.misc.raw_input', return_value='yes')
    def test_query_yes_no_true(self, mock_stdout):
        response = query_yes_no("some question")
        self.assertTrue(response)

    @mock.patch('statusdb.tools.misc.raw_input', return_value='no')
    def test_query_yes_no_false(self, mock_stdout):
        response = query_yes_no("some question")
        self.assertFalse(response)

    @mock.patch('statusdb.tools.misc.raw_input', return_value='') #Should return the default which is yes
    def test_query_yes_no_empty(self, mock_stdout):
        response = query_yes_no("some question")
        self.assertTrue(response)

    def test_query_yes_no_empty(self):
        with self.assertRaises(ValueError):
            response = query_yes_no("some question", default="invalid")

    def test_merge(self):
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 1, "c": 2}
        d3 = {"d": 3, "e": 4}
        d4 = {"f": 5, "g": 6}
        merged_dict1 = merge(d1, d2)
        merged_dict2 = merge(d3, d4)
        self.assertDictEqual(merged_dict1, {'a': 1, 'c': 2, 'b': 2})
        self.assertDictEqual(merged_dict2, {'e': 4, 'd': 3, 'g': 6, 'f': 5})
