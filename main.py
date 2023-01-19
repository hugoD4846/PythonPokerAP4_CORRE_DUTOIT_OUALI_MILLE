from card_deck import Card, Deck, Color, Value
from combinaison import Combinaison
from finder import find_combinaisons

# def find_combinaisons(hand):
#     value_int_mapping = {value: value.value for value in Value}
#     values = [value_int_mapping[card._value] for card in hand]
#     values_count = dict(collections.Counter(values))
#     colors = [card._color for card in hand]
#     colors_count = dict(collections.Counter(colors))
#     max_color_count = max(colors_count.values())
#     max_value_count = max(values_count.values())
#     is_flush = max_color_count >= 5
#     values_set = set(values)
#     is_straight = False
#     if len(values_set) >= 5:
#         if (max(values_set) - min(values_set) == 4 and len(values_set) == 5) or (values_set == {2, 3, 4, 5, 14}):
#             is_straight = True
#     if is_flush and is_straight:
#         return Combinaison.SUITE_COULEUR
#     elif max_value_count == 4:
#         return Combinaison.CARRE
#     elif max_value_count == 3:
#         if len([val for val in values_count.values() if val == 2]) == 1:
#             return Combinaison.FULL
#         else:
#             return Combinaison.BRELAN
#     elif max_value_count == 2:
#         if len([val for val in values_count.values() if val == 2]) == 2:
#             return Combinaison.DOUBLE_PAIRES
#         else:
#             return Combinaison.PAIRE
#     elif is_flush:
#         return Combinaison.COULEUR
#     elif is_straight:
#         return Combinaison.SUITE
#     else:
#         return Combinaison.RIEN


for i in range(100):
    d = Deck()
    h = [d.pop() for _ in range(7)]
    res = find_combinaisons(h)
    print(res)
