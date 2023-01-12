import enum
import random

class Value(enum.Enum):
    UN=1
    DEUX=2
    TROIS=3
    QUATRE=4
    CINQ=5
    SIX=6
    SEPT=7
    HUIT=8
    NEUF=9
    DIX=10
    VALET=11
    DAME=12
    ROI=13
    AS=14


class Color(enum.Enum):
    T="trefle"
    P="pique"
    C="coeur"
    K="carreau"

class Card:

    def __init__(self, value, color):
        if not isinstance(value, Value):
            raise TypeError(f"value must be a 'Value'")
        if not isinstance(color, Color):
            raise TypeError(f"color must be a 'Color'")
        self._value = value
        self._value2str()
        self._color = color

    def _value2str(self):
        if self._value is Value.VALET:
            self._value_str = "V"
        elif self._value is Value.DAME:
            self._value_str = "D"
        elif self._value is Value.ROI:
            self._value_str = "R"
        elif self._value is Value.AS:
            self._value_str = "A"
        else:
            self._value_str = self._value.value

    def __str__(self):
        return f"({self._value_str},{self._color.name})"

    def __repr__(self):
        return f"<{self.__str__()} at {hex(id(self))}>"

    def __lt__(self, other):
        if isinstance(other, Card):
            return self._value.value < other._value.value
        elif isinstance(other, int):
            return self._value < other
        raise ValueError(f"'other' muste be a Card or an integer, not a {other.__class__.__name__!a}")

class Deck:
    def __init__(self):
        self._cards = [Card(v, c)  for c in Color for v in Value if v is not Value.UN]
        random.shuffle(self._cards)

    def __str__(self):
        return f"Game of {len(self._cards)} cards"

    def __iter__(self):
        return iter(self._cards)

    def pop(self):
        return self._cards.pop()

    def push(self, card):
        if not isinstance(card, Card):
            raise TypeError("card must be a 'Card'")
        if card not in self._cards:
            self._cards.append(card)

    def extend(self, cards):
        if not isinstance(cards, (list, tuple, dict, set, frozenset)):
            raise TypeError("Cards must be a list, a tuple,a dict (only keys) or a set")

        if not all(isinstance(card, Card) for card in cards):
            raise TypeError("Item from cards must be a 'Card'")
        for card in cards:
            self.push(card)

    def __iadd__(self, cards):
        """call on `+=` operator"""
        self.extend(cards)
        return self