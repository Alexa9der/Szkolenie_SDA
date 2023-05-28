import unittest
from unittest.mock import MagicMock


def multiplay( a, b ):
    return a * b


class Tests(unittest.TestCase):

    def test_multyply( self ):
        self.assertEqual(multiplay(0, 1), 0)
        self.assertEqual(multiplay(2, 3), 6)
        self.assertEqual(multiplay(-2, 3), -6)

    def test_multyply_1( self ):
        self.assertNotEqual(multiplay(0, 1), 1)
        self.assertNotEqual(multiplay(2, 3), 9)

    def test_User_fing( self ):
        User.find_user = MagicMock(return_value=["Adam", "Jacek", "Kamil"])
        new_user = User()
        print(new_user.name)
        self.assertEqual(new_user.print_all_users(), ["Adam", "Jacek", "Kamil"])


class User:
    def __init__( self, name="Bil" ):
        self.name = name

    def save( self ):
        with open('testFile.txt', 'w') as file:
            file.write(self.name)

    def find_user( self ):
        with open('testFile.txt', 'r') as file:
            temp_users = file.readlines()
        return temp_users

    def print_all_users( self ):
        users = self.find_user()
        return users


if __name__ == "__main__":
    unittest.main()
