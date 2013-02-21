import unittest

class BasicTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(1,1)

    def test_2(self):
        self.assertEqual(2,2)
