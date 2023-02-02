from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
import collections
import logging


def getHashCodeFromTuple(tuple):
    tmp = str(tuple[0].value)
    if not hasattr(tuple[1], '__iter__'):
        tmp += str(tuple[1].value)
    else : 
        for elem in tuple[1] :
            if(type(elem.value) == int):
                if(elem.value < 10):
                    tmp += "0"
                tmp += str(elem.value)
    i = len(tmp)
    for i in range(0, 11 - len(tmp)):
        tmp += "0"
    return tmp
    
''' Returns a tuple containing a four of a kind and the highest card remaining in the hand '''


def get_four_of_a_kind(values_count, values):
    logging.info("get_four_of_a_kind, values_count: %s, values: %s",
                 values_count, values)
    four_of_a_kind_value = max(
        [value for value in values_count.keys() if values_count[value] == 4])
    remaining_card_value = max(
        [value for value in values if value != four_of_a_kind_value])
    logging.debug("Four of a kind value: %s", four_of_a_kind_value)
    logging.debug("Remaining card value: %s", remaining_card_value)
    return (Combinaison.CARRE, (Value(four_of_a_kind_value), Value(remaining_card_value)))


''' Return a tuple containing a full, the height of the three of a kind and the height of the pair '''


def get_full(values_count):
    logging.info("get_full, values_count: %s", values_count)
    three_of_a_kind_value = max(
        [value for value in values_count.keys() if values_count[value] == 3])
    pair_value = min(
        [value for value in values_count.keys() if values_count[value] == 2])
    logging.debug("Three of a kind value: %s", three_of_a_kind_value)
    logging.debug("Pair value: %s", pair_value)
    return (Combinaison.FULL, (Value(three_of_a_kind_value), Value(pair_value)))


''' Returns a tuple containing a flush and the cards in the flush, sorted from highest to lowest '''


def get_flush(colors_count, values, colors):
    logging.info("get_flush, colors_count: %s, values: %s, colors: %s",
                 colors_count, values, colors)
    flush_color = max(colors_count, key=colors_count.get)
    flush_values = sorted([value for value in values if colors[values.index(
        value)] == flush_color], reverse=True)
    values_flush = [Value(value) for value in flush_values]
    values_flush.insert(0, Color(flush_color))
    return (Combinaison.COULEUR, tuple(values_flush))


''' Returns a tuple containing a straight and the highest card in the straight '''


def get_straight(values):
    logging.info("get_straight, values: %s", values)
    return (Combinaison.SUITE, Value(is_straight(values)))


''' Returns a tuple containing a straight flush , the color of it and the highest card in the straight flush '''


def get_straight_flush(colors_count, values):
    logging.info("get_straight_flush, colors_count: %s, values: %s",
                 colors_count, values)
    flush_color = max(colors_count, key=colors_count.get)
    logging.debug("Flush color: %s", flush_color)
    logging.debug("Values: %s", values)
    return (Combinaison.SUITE_COULEUR, (Color(flush_color), Value(is_straight(values))))


''' Returns a tuple containg a three of a kind and the two highest cards remaining in the hand'''


def get_three_of_a_kind(values_count, values):
    logging.info("get_three_of_a_kind, values_count: %s, values: %s",
                 values_count, values)
    three_of_a_kind_value = max(
        [value for value in values_count.keys() if values_count[value] == 3])
    tuple_values = [Value(three_of_a_kind_value)]
    remaining_values = sorted(
        [value for value in values if value != three_of_a_kind_value], reverse=True)
    tuple_values = tuple_values + \
        [Value(remaining_values[0]), Value(remaining_values[1])]
    logging.debug("Three of a kind value: %s", three_of_a_kind_value)
    logging.debug("Remaining values: %s", remaining_values)
    return (Combinaison.BRELAN, tuple(tuple_values))


''' Returns a tuple containing the highest cards in the hand'''


def get_highest_cards(values):
    logging.info("get_highest_cards, values: %s", values)
    values_nothing = sorted(values, reverse=True)
    tmp = [Value(value) for value in values_nothing[:5]]
    logging.debug("Highest cards: %s", tuple(tmp))
    return (Combinaison.RIEN, tuple(tmp))


''' Returns a tuple containing two pairs, the height of the pairs sorted from highest to lowest and the highest card remaining in the hand'''


def get_double_pair(values_count):
    logging.info("get_double_pair, values_count: %s", values_count)
    pairs = []
    for value, count in values_count.items():
        if count == 2:
            pairs.append(value)
    pairs.sort(reverse=True)
    tuple_of_values = [Value(pairs) for pairs in pairs[:3]]  # 2 pairs AS Value
    for value, count in values_count.items():
        if count != 2:
            # adding remaining card to the tuple
            tuple_of_values.append(Value(value))
            break
    logging.debug("Double pairs: %s", tuple(tuple_of_values))
    return (Combinaison.DOUBLE_PAIRES, (tuple(tuple_of_values)))


''' Returns a tuple containg a pair, its value and the three highest cards remaining in the hand'''


def get_pair(values_count):
    logging.info("get_pair, values_count: %s", values_count)
    pair_value = [k for k, v in values_count.items() if v == 2]
    other_values = sorted(
        [k for k, v in values_count.items() if v != 2], reverse=True)
    tuple_of_values = [Value(high_cards)
                       for high_cards in other_values[:3]]  # 3 highest cards
    # adding pair value to the tuple
    tuple_of_values.insert(0, Value(pair_value[0]))
    logging.debug("Pair value: %s", tuple(tuple_of_values))
    return (Combinaison.PAIRE, (tuple(tuple_of_values)))


''' Takes a list of cards and returns a tuple of the best combinaison possible with those cards'''


def find_combinaisons(hand):
    logging.info("find_combinaisons, hand: %s", hand)
    if (not all(isinstance(card, Card) for card in hand)):
        logging.error(msg="hand is not a list of Card")
        raise TypeError("hand is not a list of Card")
    values = [card._value.value for card in hand]
    colors = [card._color.value for card in hand]
    values_count = dict(collections.Counter(values))
    colors_count = dict(collections.Counter(colors))

    if is_flush(colors_count) and is_straight(values):
        return get_straight_flush(colors_count, values)
    elif is_four_of_a_kind(values_count):
        return get_four_of_a_kind(values_count, values)
    elif is_full(values_count):
        return get_full(values_count)
    elif is_flush(colors_count):
        return get_flush(colors_count, values, colors)
    elif is_straight(values):
        return get_straight(values)
    elif is_three_of_a_kind(values_count):
        return get_three_of_a_kind(values_count, values)
    elif is_two_pairs(values_count):
        return get_double_pair(values_count)
    elif is_pair(values_count):
        return get_pair(values_count)
    else:  # if the hand contains no combinaison, we return the highest cards
        return get_highest_cards(values)


''' Returns True if the hand is a flush, False otherwise '''


def is_flush(colors_count):
    logging.info("is_flush, colors_count: %s", colors_count)
    max_color_count = max(colors_count.values())
    return max_color_count >= 5


''' Returns True if the hand contains a four of a kind, False otherwise '''


def is_four_of_a_kind(values_count):
    logging.info("is_four_of_a_kind, values_count: %s", values_count)
    max_value_count = max(values_count.values())
    return max_value_count == 4


''' Returns True if the hand contains a full, False otherwise'''


def is_full(values_count):
    logging.info("is_full, values_count: %s", values_count)
    values_count_list = list(values_count.values())
    # left part checks if its a full with a 3 of a kind and a pair, second part checks if hand contains two three of a kind, which corresponds to a full too!
    return ((3 in values_count_list) and (2 in values_count_list) or values_count_list.count(3) == 2)


''' Returns True if the hand contains a three of a kind, False otherwise '''


def is_three_of_a_kind(values_count):
    logging.info("is_three_of_a_kind, values_count: %s", values_count)
    max_value_count = max(values_count.values())
    return max_value_count == 3


''' Returns True if the hand contains two pairs, False otherwise'''


def is_two_pairs(values_count):
    logging.info("is_two_pairs, values_count: %s", values_count)
    values_count_list = list(values_count.values())
    return (values_count_list.count(2) >= 2)


''' Returns True if the hand contains a pair, False otherwise'''


def is_pair(values):
    logging.info("is_pair, values: %s", values)
    values_count = collections.Counter(values)
    max_value_count = max(values_count.values())
    return max_value_count == 2


''' Returns True if the hand contains a straight, False otherwise'''


def is_straight(values):
    logging.info("is_straight, values: %s", values)
    if len(values) < 5:
        return False
    values_set = set(values)
    if len(values_set) < 5:
        return False
    if 14 in values_set:
        values_set.add(1)
    for j in values_set:
        test = True
        for i in range(j+1, j + 5):
            if i not in values_set:
                test = 0
        if test:
            if (i + 2 in values_set and i + 1 in values_set):
                return i+2
            if (i + 1 in values_set):
                return i+1
            return i
    return test
