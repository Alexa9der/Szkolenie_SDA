import unittest
from ukrywanie_hasla import hide_password


class TestHiddenPassword(unittest.TestCase):

    def test_password_len_divisible_by_3(self):
        password = "password1234"
        hidden_password = hide_password(password)
        self.assertEqual(hidden_password, "pa*sw*rd*23*")

    def test_no_password(self):
        password = ""
        hidden_password = hide_password(password)
        self.assertEqual(hidden_password, "")

    def test_password_len_divisible_by_3_minus_1(self):
        password = "password123"
        hidden_password = hide_password(password)
        self.assertEqual(hidden_password, "pa*sw*rd*23")

    def test_password_len_divisible_by_3_minus_2(self):
        password = "password12"
        hidden_password = hide_password(password)
        self.assertEqual(hidden_password, "pa*sw*rd*2")

    def test_password_mega_length(self):
        password = "a"*300
        hidden_password = hide_password(password)
        self.assertTrue(hidden_password.count("*") == 100)


if __name__ == '__main__':
    unittest.main()
