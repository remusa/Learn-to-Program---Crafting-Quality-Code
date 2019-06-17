import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_k_is_zero(self):
        """Test swap_k with a list of numbers and k == 0"""

        actual = a1.swap_k([6, 7, 8, 9, 10, 11], 0)
        expected = [6, 7, 8, 9, 10, 11]
        self.assertEqual(expected, actual)

    def test_k_is_one(self):
        """Test swap_k with a list of numbers and k == 1"""

        actual = a1.swap_k([6, 7, 8, 9, 10, 11], 0)
        expected = [6, 7, 8, 9, 10, 11]
        self.assertEqual(expected, actual)

    def test_k_is_even(self):
        """Test swap_k with a list of numbers and k is an even number (2)"""

        actual = a1.swap_k([1, 2, 3, 4, 5, 6], 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected, actual)

    def test_k_is_odd(self):
        """Test swap_k with a list of numbers and k is an odd number (3)"""

        actual = a1.swap_k([6, 7, 8, 9, 10, 11], 3)
        expected = [9, 10, 11, 6, 7, 8]
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
