import unittest
import app

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(app.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(app.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(app.divide(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
