import unittest

class FailureTest(unittest.TestCase):
    def test_it(self):
        self.assertTrue(False)

    def test_exc(self):
        raise Exception

    def test_success(self):
        self.assertTrue(True)
