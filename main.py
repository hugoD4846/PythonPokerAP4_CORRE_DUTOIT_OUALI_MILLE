from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons
from logConf import setUpLogging
import logging


if __name__ == "__main__":
    setUpLogging(logging.INFO)
    for i in range(100):
        d = Deck()
        h = [d.pop() for _ in range(7)]
        logging.info("")
        res = find_combinaisons(h)
        print(res)
