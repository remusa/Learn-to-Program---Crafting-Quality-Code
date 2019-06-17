import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_zero(self):
        """Test num_buses with 0 people."""

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_one(self):
        """Test num_buses with 1 people."""

        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_fifty(self):
        """Test num_buses with 50 people."""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_less_than_fifty(self):
        """Test num_buses with less than 50 people."""

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected, actual)

    def test_one_more_multiple_fifty(self):
        """Test num_buses with more than 50 people."""

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)

    def test_multiple_fifty(self):
        """Test num_buses with a multiple of 50."""

        actual = a1.num_buses(150)
        expected = 3
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main(exit=False)
