import unittest
from statusdb.tools.log import minimal_logger

class TestLog(unittest.TestCase):
    def test_minimal_logger(self):
        logger = minimal_logger("some_log")
        assert logger is not None
