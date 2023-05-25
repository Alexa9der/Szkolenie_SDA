"""
    Dla funkcji odd_indexes napisanej ponizej,
    ktora dla zadanego stringa zwraca litery z nieparzystych indeksow, np:
    - teleturniej -> eeune
    - komputer -> optr,

    napisz testy dla argumentu, ktory bedzie stringiem.

    Uruchom funkcje przekazujac int.
    Zaobserwuj, co sie stalo.
    Napisz testy dla argumentow, ktore sa intem.
    Popraw funkcje by dzialala poprawnie, sprawiajac by testy przeszly.
"""

import unittest


def odd_indexes( string ):
    return string[1::2]


class TestOddIndexes(unittest.TestCase):

    def test_equal_odd_indexes( self ):
        self.assertEqual(odd_indexes("teleturniej"), "eeune")
        self.assertEqual(odd_indexes("komputer"), "optr")

    def test_raises_odd_indexes( self ):
        # check that odd_indexes fails when the argument is int
        with self.assertRaises(TypeError):
            odd_indexes(123)

        with self.assertRaises(AssertionError):
            self.assertEqual(odd_indexes("komputer"), "opt")

        ...


if __name__ == "__main__":
    unittest.main()
