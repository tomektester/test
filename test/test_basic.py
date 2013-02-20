import unittest

class BasicTest(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1,1)
