import unittest
from main import max_of_three_vars


class MaxOfThreeVarsTestCase(unittest.TestCase):
    def test_max_a(self):
        res = max_of_three_vars(3, 2, 1)
        self.assertEqual(3, res)

    def test_max_b(self):
        res = max_of_three_vars(2, 3, 1)
        self.assertEqual(3, res)

    def test_max_c(self):
        res = max_of_three_vars(1, 2, 3)
        self.assertEqual(3, res)

    def test_max_equal(self):
        res = max_of_three_vars(1, 1, 1)
        self.assertEqual(None, res)
