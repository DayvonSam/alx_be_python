import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a new SimpleCalculator instance for each test."""
        self.calc = SimpleCalculator()

    # Addition tests
    def test_add_positive_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 1.2), 3.7, places=7)

    # Subtraction tests
    def test_subtract_positive_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    # Multiplication tests
    def test_multiply_positive_integers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)

    # Division tests
    def test_divide_positive_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)

    def test_divide_resulting_float(self):
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25, places=7)

    def test_divide_negative(self):
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5.0, places=7)
        self.assertAlmostEqual(self.calc.divide(10, -2), -5.0, places=7)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    # Additional sanity checks
    def test_commutativity_add_and_multiply(self):
        # add is commutative
        self.assertEqual(self.calc.add(3, 7), self.calc.add(7, 3))
        # multiply is commutative
        self.assertEqual(self.calc.multiply(3, 7), self.calc.multiply(7, 3))

    def test_associative_like_behaviour_add(self):
        # basic associative-like check for add ( (a + b) + c == a + (b + c) )
        a, b, c = 1, 2, 3
        self.assertEqual(self.calc.add(self.calc.add(a, b), c),
                         self.calc.add(a, self.calc.add(b, c)))

if __name__ == "__main__":
    unittest.main()
