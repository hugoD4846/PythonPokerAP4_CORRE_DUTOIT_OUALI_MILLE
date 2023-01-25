from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons, is_straight, is_full, is_pair, is_flush, is_two_pairs, is_four_of_a_kind, is_three_of_a_kind
import unittest
import collections


class TestCombinations(unittest.TestCase):

    def test_is_two_pairs(self):
        # Test with three pairs
        values = [2, 2, 3, 3, 6, 6, 5]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_two_pairs(values_dict) == expected_output
        # Test with two pairs
        values = [2, 5, 3, 3, 5, 1, 7]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_two_pairs(values_dict) == expected_output
        # Test with a single pair
        values = [2, 14, 3, 3, 5, 1, 8]
        values_dict = dict(collections.Counter(values))
        expected_output = False
        assert is_two_pairs(values_dict) == expected_output

    def test_quinte_flush(self):
        hand = [Card(Value.SEPT, Color.P), Card(Value.HUIT, Color.P), Card(Value.NEUF, Color.P),
                Card(Value.DIX, Color.P), Card(
            Value.VALET, Color.P), Card(Value.QUATRE, Color.C),
            Card(Value.DIX, Color.K)]
        self.assertEqual(find_combinaisons(
            hand), (Combinaison.SUITE_COULEUR, (Color.P, Value.VALET)))

    def test_is_flush(self):
        # TEST WITH FLUSH
        values = [Color.C, Color.C, Color.C,
                  Color.C, Color.C, Color.T, Color.T]
        colors_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_flush(colors_dict) == expected_output
        # TEST WITH NO FLUSH
        values = [Color.T, Color.C, Color.C,
                  Color.C, Color.C, Color.T, Color.T]
        colors_dict = dict(collections.Counter(values))
        expected_output = False
        assert is_flush(colors_dict) == expected_output

    def test_is_three_of_a_kind(self):
        # TEST WITH TWO THREE OF A KIND
        values = [14, 14, 14, 3, 4, 3, 3]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_three_of_a_kind(values_dict) == expected_output
        # TEST WITH THREE OF A KIND
        values = [14, 14, 14, 2, 4, 5, 3]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_three_of_a_kind(values_dict) == expected_output
        # TEST WITH TWO PAIRS
        values = [14, 2, 3, 3, 4, 5, 5]
        values_dict = dict(collections.Counter(values))
        expected_output = False
        assert is_three_of_a_kind(values_dict) == expected_output

    def test_is_full(self):
        # TEST WITH A FULL
        values = [14, 14, 14, 4, 4, 5, 7]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_full(values_dict) == expected_output
        # TEST WITH THREE OF A KIND
        values = [14, 3, 3, 3, 4]
        values_dict = dict(collections.Counter(values))
        expected_output = False
        assert is_full(values_dict) == expected_output
        # TEST WITH 2 THREE OF A KIND
        values = [14, 14, 14, 4, 4, 5, 4]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_full(values_dict) == expected_output

    def test_is_four_of_a_kind(self):
        # TEST WITH A FOUR OF A KIND
        values = [14, 14, 14, 14, 4, 2, 3]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_four_of_a_kind(values_dict) == expected_output
        # TEST WITH 2 THREE OF A KIND
        values = [14, 3, 3, 3, 4, 4, 4]
        values_dict = dict(collections.Counter(values))
        expected_output = False
        assert is_four_of_a_kind(values_dict) == expected_output
        # TEST WITH A FOUR OF A KIND AND A THREE OF A KIND
        values = [3, 3, 3, 3, 4, 4, 4]
        values_dict = dict(collections.Counter(values))
        expected_output = True
        assert is_four_of_a_kind(values_dict) == expected_output

    def test_is_pair(self):
        # Test with a valid pair
        values = [2, 2, 3, 4, 5, 9, 10]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with a valid pair of aces
        values = [14, 14, 2, 3, 4, 9, 8]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with no pair
        values = [2, 3, 4, 5, 6, 10, 11]
        expected_output = False
        assert is_pair(values) == expected_output

        # Test with two pairs
        values = [2, 2, 3, 3, 5, 7, 9]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with three pairs
        values = [2, 2, 3, 3, 5, 5, 9]
        expected_output = True
        assert is_pair(values) == expected_output

    def test_is_straight(self):
        # Test with a valid straight
        values = [2, 3, 4, 5, 6, 10, 11]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with a valid Ace-low straight
        values = [14, 5, 4, 3, 2, 8, 9]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with less than 5 cards
        values = [2, 3, 4]
        expected_output = False
        assert is_straight(values) == expected_output

        # Test with non-consecutive cards
        values = [2, 3, 7, 8, 9, 8, 9]
        expected_output = False
        assert is_straight(values) == expected_output

        # Test with duplicate cards
        values = [2, 3, 4, 5, 2, 9, 11]
        expected_output = False
        assert is_straight(values) == expected_output

        # Test with duplicate cards
        values = [7, 8, 9, 10, 11, 4, 13]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with duplicate cards
        values = [10, 11, 12, 13, 13, 14, 13]
        expected_output = True
        assert is_straight(values) == expected_output


if __name__ == '__main__':
    unittest.main()
