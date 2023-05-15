import unittest
from liczby_pierwsze import is_prime_number


class TestPrimeNumbers(unittest.TestCase):

    def test_0_as_not_a_prime_number(self):
        self.assertIs(is_prime_number(0), False)

    def test_1_as_not_a_prime_number(self):
        self.assertIs(is_prime_number(1), False)

    def test_2_as_a_prime_number(self):
        self.assertIs(is_prime_number(2), True)

    def test_3_as_a_prime_number(self):
        self.assertIs(is_prime_number(3), True)

    def test_6_as_not_a_prime_number(self):
        self.assertIs(is_prime_number(6), False)

    def test_19_as_a_prime_number(self):
        self.assertIs(is_prime_number(19), True)

    def test_50_as_not_a_prime_number(self):
        self.assertIs(is_prime_number(50), False)


if __name__ == '__main__':
    unittest.main()
