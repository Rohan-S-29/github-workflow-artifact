import unittest
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(math.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(math.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(math.divide(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
