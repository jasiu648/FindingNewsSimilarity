import unittest

# The class to be tested
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# The test case class
class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This method is called before each test method
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)  # Assert that the result is equal to 5

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)  # Assert that the result is equal to 2

    def test_add_negative_numbers(self):
        result = self.calculator.add(-2, -3)
        self.assertEqual(result, -5)  # Assert that the result is equal to -5

