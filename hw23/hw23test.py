from hw23 import *
import unittest


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculator.nums_sum(6, 2), 8)

    def test_sub(self):
        self.assertEqual(Calculator.nums_sub(6, 2), 4)

    def test_mult(self):
        self.assertEqual(Calculator.nums_mult(6, 2), 12)

    def test_div(self):
        self.assertEqual(Calculator.nums_div(6, 2), 3)

    def test_zero_div(self):
        self.assertIsNone(Calculator.nums_div(6, 0))

    def test_max(self):
        self.assertEqual(Calculator.nums_max(6, 2), 6)

    def test_min(self):
        self.assertEqual(Calculator.nums_min(6, 2), 2)

    def test_sqr(self):
        self.assertEqual(Calculator.nums_sqr(6, 2), 36)

    def test_prec(self):
        self.assertEqual(Calculator.nums_prec(50, 12), 6)


class FactorialTest(unittest.TestCase):
    def test_common(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_argument(self):
        self.assertRaises(ValueError, factorial, -5)

    def test_diff_type(self):
        self.assertRaises(ValueError, factorial, 6.496)
