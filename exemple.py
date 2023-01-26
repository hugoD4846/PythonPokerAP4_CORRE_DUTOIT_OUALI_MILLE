from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons

if __name__ == "__main__":
    deck = Deck() # create a deck
    hand = [deck.pop() for _ in range(7)] # get 7 cards from the deck to create an hand and remove them from the deck  with pop() method
    combinaison = find_combinaisons(hand) # find combinaisons in the hand
    print(combinaison) # print the result

