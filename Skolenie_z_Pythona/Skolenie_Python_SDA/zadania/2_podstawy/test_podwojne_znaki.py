import unittest
from podwojne_znaki import produce_double_signs


class TestDoubleSigns(unittest.TestCase):

    def test_python_string_written_in_small_letters(self):
        double_string = produce_double_signs("python")
        self.assertEqual(double_string, "ppyytthhoonn")

    def test_python_string_written_in_small_and_big_letters(self):
        double_string = produce_double_signs("PyThoN")
        self.assertEqual(double_string, "PPyyTThhooNN")

    def test_one_letter_string(self):
        double_string = produce_double_signs("X")
        self.assertEqual(double_string, "XX")

    def test_double_signs_output_for_empty_string(self):
        double_string = produce_double_signs("")
        self.assertEqual(double_string, "")


if __name__ == '__main__':
    unittest.main()
