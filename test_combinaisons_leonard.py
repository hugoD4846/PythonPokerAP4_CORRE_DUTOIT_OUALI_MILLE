# from card_deck import Card, Deck, Color, Value
# from combinaison import Combinaison
# import collections


# def test_SUITE():
#     h = [Card(Color.P, Value.VALET), Card(Color.P, Value.DAME), Card(Color.P, Value.ROI), Card(Color.P, Value.DIX), Card(Color.P, Value.HUIT)]


# def test_BRELAN():
#     h = [Card(Color.P, Value.VALET), Card(Color.C, Value.VALET), Card(Color.T, Value.VALET), Card(Color.P, Value.DIX), Card(Color.P, Value.HUIT)]


# def test_DOUBLE_PAIRES():
#     h = [Card(Color.P, Value.VALET), Card(Color.C, Value.VALET), Card(Color.T, Value.ROI), Card(Color.P, Value.ROI), Card(Color.P, Value.HUIT)]

# def test_PAIRE():
#     h = [Card(Color.P, Value.VALET), Card(Color.C, Value.VALET), Card(Color.T, Value.ROI), Card(Color.P, Value.DIX), Card(Color.P, Value.HUIT)]


from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons, is_straight, is_pair
import unittest


class TestCombinations(unittest.TestCase):
    def test_suite_couleur(self):
        # create a hand of 7 cards that forms a straight flush
        hand = [Card(Value.DEUX, Color.P), Card(Value.TROIS, Color.P), Card(Value.QUATRE, Color.P),
                Card(Value.CINQ, Color.P), Card(
                    Value.SIX, Color.P), Card(Value.SEPT, Color.P),
                Card(Value.HUIT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.SUITE_COULEUR)

    def test_carre(self):
        # create a hand of 7 cards that forms a four of a kind
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.DEUX, Color.T),
                Card(Value.DEUX, Color.K), Card(
                    Value.CINQ, Color.P), Card(Value.SIX, Color.P),
                Card(Value.SEPT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.CARRE)

    def test_full(self):
        # create a hand of 7 cards that forms a full
        hand = [Card(Value.ROI, Color.P), Card(Value.ROI, Color.C), Card(Value.ROI, Color.T),
                Card(Value.DIX, Color.K), Card(
                    Value.DIX, Color.P), Card(Value.QUATRE, Color.C),
                Card(Value.SEPT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.FULL)

    def test_brelan(self):
        # create a hand of 7 cards that forms a three of a kind
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.DEUX, Color.T),
                Card(Value.QUATRE, Color.K), Card(
                    Value.CINQ, Color.P), Card(Value.SIX, Color.P),
                Card(Value.SEPT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.BRELAN)

    def test_double_paires(self):
        # create a hand of 7 cards that forms a two pairs
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.TROIS, Color.T),
                Card(Value.TROIS, Color.K), Card(
                    Value.CINQ, Color.P), Card(Value.SIX, Color.P),
                Card(Value.SEPT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.DOUBLE_PAIRES)

    def test_paire(self):
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.TROIS, Color.T),
                Card(Value.QUATRE, Color.K), Card(
                    Value.CINQ, Color.P), Card(Value.DIX, Color.P),
                Card(Value.SEPT, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.PAIRE)

    def test_couleur(self):
        hand = [Card(Value.DEUX, Color.P), Card(Value.QUATRE, Color.P), Card(Value.SIX, Color.P),
                Card(Value.HUIT, Color.P), Card(
                    Value.DIX, Color.P), Card(Value.VALET, Color.P),
                Card(Value.DAME, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.COULEUR)

    def test_suite(self):
        hand = [Card(Value.DEUX, Color.P), Card(Value.TROIS, Color.C), Card(Value.QUATRE, Color.T),
                Card(Value.CINQ, Color.K), Card(
                    Value.SIX, Color.K), Card(Value.DAME, Color.P),
                Card(Value.DIX, Color.P)]
        self.assertEqual(find_combinaisons(hand), Combinaison.SUITE)

    def test_carre(self):
        # Test with a valid carre
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.DEUX, Color.T), Card(Value.DEUX, Color.K),
                Card(Value.CINQ, Color.K), Card(Value.DAME, Color.P), Card(Value.DIX, Color.P)]
        expected_output = Combinaison.CARRE
        assert find_combinaisons(hand) == expected_output

        # Test with 4 aces
        hand = [Card(Value.AS, Color.P), Card(Value.AS, Color.C), Card(Value.AS, Color.T), Card(Value.AS, Color.K),
                Card(Value.CINQ, Color.K), Card(Value.DAME, Color.P), Card(Value.DIX, Color.P)]
        expected_output = Combinaison.CARRE
        assert find_combinaisons(hand) == expected_output

        # Test with a three of a kind and a pair
        hand = [Card(Value.DEUX, Color.P), Card(Value.DEUX, Color.C), Card(Value.DEUX, Color.T), Card(Value.CINQ, Color.K),
                Card(Value.CINQ, Color.K), Card(Value.DAME, Color.P), Card(Value.DIX, Color.P)]
        expected_output = Combinaison.BRELAN
        assert find_combinaisons(hand) == expected_output

    def test_is_pair(self):
        # Test with a valid pair
        values = [2, 2, 3, 4, 5]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with a valid pair of aces
        values = [14, 14, 2, 3, 4]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with less than 5 cards
        values = [2, 2, 3, 4]
        expected_output = False
        assert is_pair(values) == expected_output

        # Test with no pair
        values = [2, 3, 4, 5, 6]
        expected_output = False
        assert is_pair(values) == expected_output

        # Test with a pair and a three of a kind
        values = [2, 2, 2, 4, 5]
        expected_output = True
        assert is_pair(values) == expected_output

        # Test with two pairs
        values = [2, 2, 3, 3, 5]
        expected_output = True
        assert is_pair(values) == expected_output

    def test_is_straight(self):
        # Test with a valid straight
        values = [2, 3, 4, 5, 6]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with a valid Ace-low straight
        values = [14, 5, 4, 3, 2]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with a valid Ace-low straight
        values = [14, 2, 3, 4, 5]
        expected_output = True
        assert is_straight(values) == expected_output

        # Test with less than 5 cards
        values = [2, 3, 4]
        expected_output = False
        assert is_straight(values) == expected_output

        # Test with non-consecutive cards
        values = [2, 3, 7, 8, 9]
        expected_output = False
        assert is_straight(values) == expected_output

        # Test with duplicate cards
        values = [2, 3, 4, 5, 2]
        expected_output = False
        assert is_straight(values) == expected_output


if __name__ == '__main__':
    unittest.main()
