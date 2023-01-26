from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons
from logConf import setUpLogging
import logging

if __name__ == "__main__":
    setUpLogging(logging.INFO)
    deck = Deck()  # create a deck
    # get 7 cards from the deck to create an hand and remove them from the deck  with pop() method
    hand = [deck.pop() for _ in range(7)]
    combinaison = find_combinaisons(hand)  # find combinaisons in the hand
    print(combinaison)  # print the result
