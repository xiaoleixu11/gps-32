"""Module providing a function printing python version."""

import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Class representing something"""

    def test_is_upper(self):
        """Function test_is_upper."""
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """Function test_is_lower."""
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """Function test_is_capitalize."""
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()
