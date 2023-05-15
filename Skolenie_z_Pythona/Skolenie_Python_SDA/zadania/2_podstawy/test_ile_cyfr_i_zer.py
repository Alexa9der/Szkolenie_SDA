import unittest
from ile_cyfr_i_zer import count_digits, count_zeros


class TestDigits(unittest.TestCase):

    def test_one_digit(self):
        self.assertEqual(count_digits(1), 1)

    def test_two_digits(self):
        self.assertEqual(count_digits(20), 2)

    def test_many_digits(self):
        self.assertEqual(count_digits(1234567891011), 13)


class TestZeros(unittest.TestCase):

    def test_no_zeros(self):
        self.assertEqual(count_zeros(11), 0)

    def test_one_zero(self):
        self.assertEqual(count_zeros(101), 1)

    def test_multiple_zeros(self):
        self.assertEqual(count_zeros(100010), 4)

    def test_number_only_with_zeros(self):
        self.assertEqual(count_zeros(00000), 1)


if __name__ == '__main__':
    unittest.main()
