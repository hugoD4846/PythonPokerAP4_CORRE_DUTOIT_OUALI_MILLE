from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
import collections


def find_combinaisons(hand):
    values = [card._value.value for card in hand]
    colors = [card._color.value for card in hand]
    values_count = dict(collections.Counter(values))
    colors_count = dict(collections.Counter(colors))

    if is_flush(colors_count) and is_straight(values):
        flush_color = max(colors_count, key=colors_count.get)
        return (Combinaison.SUITE_COULEUR, (Color(flush_color), Value(max(values))))
    elif is_four_of_a_kind(values_count):
        four_of_a_kind_value = max(
            [value for value in values_count.keys() if values_count[value] == 4])
        remaining_card_value = min(
            [value for value in values if value != four_of_a_kind_value])
        return (Combinaison.CARRE, four_of_a_kind_value, remaining_card_value)
    elif is_full(values_count):
        three_of_a_kind_value = max(
            [value for value in values_count.keys() if values_count[value] == 3])
        pair_value = min(
            [value for value in values_count.keys() if values_count[value] == 2])
        return (Combinaison.FULL, three_of_a_kind_value, pair_value)
    elif is_flush(colors_count):
        flush_color = max(colors_count, key=colors_count.get)
        flush_values = sorted([value for value in values if colors[values.index(
            value)] == flush_color], reverse=True)
        return (Combinaison.COULEUR, flush_color, flush_values)
    elif is_straight(values):
        return (Combinaison.SUITE, max(values))
    elif is_three_of_a_kind(values_count):
        three_of_a_kind_value = max(
            [value for value in values_count.keys() if values_count[value] == 3])
        tuple_values = [Value(three_of_a_kind_value)]
        remaining_values = sorted(
            [value for value in values if value != three_of_a_kind_value], reverse=True)
        tuple_values = tuple_values + [Value(remaining_values[0]), Value(remaining_values[1])]
        return (Combinaison.BRELAN, tuple(tuple_values))
    elif is_two_pairs(values_count):
        pairs = []
        for value, count in values_count.items():
            if count == 2:
                pairs.append(value)
        pairs.sort(reverse=True)
        tuple_of_values = [Value(pairs) for pairs in pairs[:3]] # 2 pairs AS Value
        for value, count in values_count.items():
            if count != 2:
                tuple_of_values.append(Value(value)) #adding remaining card to the tuple
                break
        return (Combinaison.DOUBLE_PAIRES, (tuple(tuple_of_values)))
    elif is_pair(values_count):
        pair_value = [k for k, v in values_count.items() if v == 2]
        other_values = sorted(
            [k for k, v in values_count.items() if v != 2], reverse=True)
        tuple_of_values = [Value(high_cards) for high_cards in other_values[:3]] # 3 highest cards
        tuple_of_values.insert(0,Value(pair_value[0])) #adding pair value to the tuple
        return (Combinaison.PAIRE, (  tuple( tuple_of_values) ))
    else:
        return (Combinaison.RIEN, sorted(values, reverse=True))


def is_flush(colors_count):
    max_color_count = max(colors_count.values())
    return max_color_count >= 5


def is_four_of_a_kind(values_count):
    max_value_count = max(values_count.values())
    return max_value_count == 4


def is_full(values_count):
    values_count_list = list(values_count.values())
    ## left part checks if its a full with a 3 of a kind and a pair, second part checks if hand contains two three of a kind, which corresponds to a full too!
    return ((3 in values_count_list) and (2 in values_count_list) or values_count_list.count(3)==2) 


def is_three_of_a_kind(values_count):
    max_value_count = max(values_count.values())
    return max_value_count == 3


def is_two_pairs(values_count):
    values_count_list = list(values_count.values())
    return (values_count_list.count(2) >= 2)


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
        values_set.add(1)
    min_value = min(values_set)
    # print(values_set)
    for j in values_set:
        test = True
        for i in range(j+1, j + 5):
            if i not in values_set:
                test = False
        if test:
            return True
    return test
