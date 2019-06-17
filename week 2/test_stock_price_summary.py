import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_combined(self):
        """Test stock_price_summary with list that has at least a zero, a positive and a negative value."""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

    def test_empty(self):
        """Test stock_price_summary with an empty list."""

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_one_zero(self):
        """Test stock_price_summary with list of one zero value."""

        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_one_positive(self):
        """Test stock_price_summary with list of one positive value."""

        actual = a1.stock_price_summary([0.03])
        expected = (0.03, 0)
        self.assertEqual(expected, actual)

    def test_one_negative(self):
        """Test stock_price_summary with list of one negative value."""

        actual = a1.stock_price_summary([-0.03])
        expected = (0, -0.03)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
