import unittest
import statusdb.tools.http as http
import mock
import os
import httplib

class TestHttp(unittest.TestCase):
    @mock.patch('statusdb.tools.http.httplib.HTTPConnection')
    def test_get_server_status_code(self, mock_get):
        mock_get.return_value.ok = 301
        test_url = 'http://some.test.url'
        current_status = http.get_server_status_code(test_url)
        assert current_status is not None

    @mock.patch('statusdb.tools.http.httplib.HTTPConnection')
    def test_check_url(self, mock_get):
        mock_get.return_value.getresponse().status = 301
        test_url = 'http://some.test.url'
        current_status = http.check_url(test_url)
        assert current_status is True
