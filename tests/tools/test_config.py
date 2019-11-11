import unittest
import statusdb.tools.config as config
import os

class TestConfig(unittest.TestCase):

    def test_load_config_valid_case(self):
        path = os.path.dirname(os.path.abspath(__file__))
        valid_config_file = os.path.join(path, '../test_data/test_statusdb.yaml')
        expected_config_data = {'statusdb': {'username': 'test.user',
                                             'url': 'some.url.se',
                                             'password': 's0mePassword!',
                                             'port': 1234}}
        got_config_data = config.load_config(valid_config_file)
        assert got_config_data == expected_config_data

    def test_load_config_file_missing(self):
        path = os.path.dirname(os.path.abspath(__file__))
        missing_config_file = os.path.join(path, '../test_data/test_missing_statusdb.yaml')
        with self.assertRaises(IOError):
            got_config_data = config.load_config(missing_config_file)
