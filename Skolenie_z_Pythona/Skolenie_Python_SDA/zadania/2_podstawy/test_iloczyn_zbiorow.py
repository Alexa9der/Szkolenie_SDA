import unittest
from iloczyn_zbiorow import find_common_numbers


class MyTestCase(unittest.TestCase):

    def test_one_empty_set(self):
        set1 = {1, 2, 3, 4}
        set2 = set()
        self.assertEqual(find_common_numbers(set1, set2), set())

    def test_two_sets_with_no_common_numbers(self):
        set1 = {1, 2, 3, 4}
        set2 = {5, 6, 7, 8}
        self.assertEqual(find_common_numbers(set1, set2), set())

    def test_two_identical_sets(self):
        set1 = set2 = {1, 2, 3, 4}
        self.assertEqual(find_common_numbers(set1, set2), set1)

    def test_two_different_sets_with_few_common_numbers(self):
        set1 = {1, 2, 3, 4}
        set2 = {2, 3, 5, 7, 9, 10}
        self.assertEqual(find_common_numbers(set1, set2), {2, 3})


if __name__ == '__main__':
    unittest.main()
