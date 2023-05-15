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


def odd_indexes(string):
    if not isinstance(string, str):
        return
    return string[1::2]


class TestOddIndexes(unittest.TestCase):

    def test_odd_indexes_nominal(self):
        self.assertEqual(odd_indexes('teleturniej'), 'eeune')
  
    def test_odd_indexes_empty_str(self):
        self.assertEqual(odd_indexes(''), '')
  
    def test_odd_indexes_one_letter(self):
        self.assertEqual(odd_indexes('a'), '')
  
    def test_odd_indexes_int(self):
        self.assertEqual(odd_indexes(5), None)


if __name__ == '__main__':
    unittest.main()
