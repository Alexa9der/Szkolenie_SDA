import unittest
from palindrom import check_if_palindrome


class TestPalindrome(unittest.TestCase):

    def test_empty_string_as_a_palindrome(self):
        string = ""
        is_palindrome = check_if_palindrome(string)
        self.assertIs(is_palindrome, True)  # Zauwaz zmiane metody: assertTrue, nie assertEqual
                                            # tutaj sprawdzamy czy is_palindrome jest True

    def test_kajak_as_a_palindrome(self):
        string = "kajak"
        is_palindrome = check_if_palindrome(string)
        self.assertIs(is_palindrome, True)

    def test_random_word_to_not_be_a_palindrome(self):
        string = "random_string"
        is_palindrome = check_if_palindrome(string)
        self.assertIs(is_palindrome, False)  # Teraz assertFalse, sprawdzamy czy random_string nie jest palindromem

    def test_word_with_even_amount_of_letters_as_a_palindrome(self):
        string = "abccba"
        is_palindrome = check_if_palindrome(string)
        self.assertIs(is_palindrome, True)


if __name__ == '__main__':
    unittest.main()
    # ok

