import unittest
from gra_w_wojne import determine_the_winner


class TestWarCardPlay(unittest.TestCase):

    def test_tie_between_cards(self):
        self.assertEqual(determine_the_winner("D", "D"), 0)

    def test_card1_wins_with_digit_card(self):
        self.assertEqual(determine_the_winner("5", "3"), 1)

    def test_card1_wins_with_figure_card(self):
        self.assertEqual(determine_the_winner("J", "8"), 1)

    def test_card1_wins_with_figure_card_vs_figure_card(self):
        self.assertEqual(determine_the_winner("A", "K"), 1)

    def test_card2_wins_with_figure_card_vs_figure_card(self):
        self.assertEqual(determine_the_winner("D", "K"), 2)

    def test_card2_wins_with_digit_card(self):
        self.assertEqual(determine_the_winner("3", "10"), 2)

    def test_ace_as_a_strongest_card(self):
        self.assertEqual(determine_the_winner("A", "2"), 1)
        self.assertEqual(determine_the_winner("A", "3"), 1)
        self.assertEqual(determine_the_winner("A", "4"), 1)
        self.assertEqual(determine_the_winner("A", "5"), 1)
        self.assertEqual(determine_the_winner("A", "6"), 1)
        self.assertEqual(determine_the_winner("A", "7"), 1)
        self.assertEqual(determine_the_winner("A", "8"), 1)
        self.assertEqual(determine_the_winner("A", "9"), 1)
        self.assertEqual(determine_the_winner("A", "10"), 1)
        self.assertEqual(determine_the_winner("A", "J"), 1)
        self.assertEqual(determine_the_winner("A", "D"), 1)
        self.assertEqual(determine_the_winner("A", "K"), 1)
        self.assertEqual(determine_the_winner("A", "A"), 0)

    def test_two_as_a_weakest_card(self):
        self.assertEqual(determine_the_winner("2", "2"), 0)
        self.assertEqual(determine_the_winner("2", "3"), 2)
        self.assertEqual(determine_the_winner("2", "4"), 2)
        self.assertEqual(determine_the_winner("2", "5"), 2)
        self.assertEqual(determine_the_winner("2", "6"), 2)
        self.assertEqual(determine_the_winner("2", "7"), 2)
        self.assertEqual(determine_the_winner("2", "8"), 2)
        self.assertEqual(determine_the_winner("2", "9"), 2)
        self.assertEqual(determine_the_winner("2", "10"), 2)
        self.assertEqual(determine_the_winner("2", "J"), 2)
        self.assertEqual(determine_the_winner("2", "D"), 2)
        self.assertEqual(determine_the_winner("2", "K"), 2)
        self.assertEqual(determine_the_winner("2", "A"), 2)
        

if __name__ == '__main__':
    unittest.main()
