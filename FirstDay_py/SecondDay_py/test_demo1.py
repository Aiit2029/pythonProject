import unittest
from caculate import MyCalculate


class TestMyCalculate(unittest.TestCase):
    def test_oppositionalities(self):
        self.assertEqual(MyCalculate(5, 3), 8)

    def test_electronegative(self):
        self.assertEqual(MyCalculate(-2, -5),-7)
