from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
import collections

def find_combinaisons(hand):
    values = [card._value for card in hand]
    print('='*20)
    print(values)
    print('='*20)
    
    # values.sort()
    values_count = dict(collections.Counter(values))
    colors = [card._color for card in hand]
    colors_count = dict(collections.Counter(colors))
    max_color_count = max(colors_count.values())
    max_value_count = max(values_count.values())
    is_flush = max_color_count >= 5
    is_straight = (values[-1].value - values[0].value == 4 and len(set(values)) == 5) or values == [Value.DEUX, Value.TROIS, Value.QUATRE, Value.CINQ, Value.AS]
    if is_flush and is_straight:
        return Combinaison.SUITE_COULEUR
    elif max_value_count == 4:
        return Combinaison.CARRE
    elif max_value_count == 3:
        if len([val for val in values_count.values() if val == 2]) == 1:
            return Combinaison.FULL
        else:
            return Combinaison.BRELAN
    elif max_value_count == 2:
        if len([val for val in values_count.values() if val == 2]) == 2:
            return Combinaison.DOUBLE_PAIRES
        else:
            return Combinaison.PAIRE
    elif is_flush:
        return Combinaison.COULEUR
    elif is_straight:
        return Combinaison.SUITE
    else:
        return Combinaison.RIEN


d = Deck()
h = [d.pop() for _ in range(7)]
res = find_combinaisons(h)

print(res)