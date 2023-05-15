import unittest
from polaczone_napisy import merge_strings


class TestMergeStrings(unittest.TestCase):

    def test_first_str_empty_other_non_emtpy(self):
        string1 = ""
        string2 = "napis"
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "napis")

    def test_first_str_non_empty_other_emtpy(self):
        string1 = "napis"
        string2 = ""
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "napis")

    def test_both_strings_are_empty(self):
        string1 = ""
        string2 = ""
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "")

    def test_strings_with_the_same_length(self):
        string1 = "mocny"
        string2 = "napis"
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "mnoacpniys")

    def test_first_str_shorter_than_other(self):
        string1 = "moc"
        string2 = "napis"
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "mnoacpis")

    def test_first_str_longer_than_other(self):
        string1 = "potezny"
        string2 = "napis"
        string3 = merge_strings(string1, string2)
        self.assertEqual(string3, "pnoatpeizsny")


if __name__ == '__main__':
    unittest.main()
