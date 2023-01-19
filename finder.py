from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
import collections


def find_combinaisons(hand):
    values = [card._value for card in hand]
    values_count = collections.Counter(values)
    values_count = dict(sorted(values_count.items(),
                        key=lambda item: item[1], reverse=True))
    values = sorted(values, key=lambda value: value.value, reverse=True)
    color = [card._color for card in hand]
    color_count = collections.Counter(color)
    color_count = dict(
        sorted(color_count.items(), key=lambda item: item[1], reverse=True))
    color = sorted(color, key=lambda color: color.name, reverse=True)
    if is_flush(color_count) and is_straight(values):
        return (Combinaison.SUITE_COULEUR, max(values).value, color[0])
    elif is_four_of_a_kind(values_count):
        return (Combinaison.CARRE, [value for value, count in values_count.items() if count == 4][0], [value for value, count in values_count.items() if count == 1][0])
    elif is_full(values_count):
        return (Combinaison.FULL, [value for value, count in values_count.items() if count == 3][0], [value for value, count in values_count.items() if count == 2][0])
    elif is_flush(color_count):
        return (Combinaison.COULEUR, color[0], [value.value for value in values])
    elif is_straight(values):
        return (Combinaison.SUITE, max(values).value)
    elif is_brelan(values_count):
        return (Combinaison.BRELAN, [value for value, count in values_count.items() if count == 3][0], [value for value, count in values_count.items() if count != 3][:2])
    elif is_double_paires(values_count):
        return (Combinaison.DOUBLE_PAIRES, [value for value, count in values_count.items() if count == 2][:2], [value for value, count in values_count.items() if count != 2][0])
    elif is_paire(values_count):
        return (Combinaison.PAIRE, [value for value, count in values_count.items() if count == 2][0], [value for value, count in values_count.items() if count != 2])
    else:
        return (Combinaison.RIEN, [value.value for value in values])


def is_flush(colors_count):
    max_color_count = max(colors_count.values())
    return max_color_count >= 5


def is_four_of_a_kind(values_count):
    max_value_count = max(values_count.values())
    return max_value_count == 4


def is_full(values_count):
    values_count_list = list(values_count.values())
    return (3 in values_count_list) and (2 in values_count_list)


def is_three_of_a_kind(values_count):
    max_value_count = max(values_count.values())
    return max_value_count == 3


def is_two_pairs(values_count):
    values_count_list = list(values_count.values())
    return (values_count_list.count(2) == 2)


def is_pair(values):
    values_count = collections.Counter(values)
    max_value_count = max(values_count.values())
    return max_value_count == 2


def is_straight(values):
    if len(values) < 5:
        return False
    values_set = set(values)
    if len(values_set) < 5:
        return False
    if 14 in values_set:
        values_set.remove(14)
        values_set.add(1)
    min_value = min(values_set)
    for i in range(min_value, min_value+5):
        if i not in values_set:
            return False
    return True
