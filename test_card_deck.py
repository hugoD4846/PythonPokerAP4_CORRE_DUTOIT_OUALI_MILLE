import enum
import sys

from card_deck import Card, Deck, Color, Value

def test_card_deck():
    datas = ( 
        (10, Color.T),
        (Value.NEUF, 12),

    )
    print(dir(Color))
    c1 = Card(Value.NEUF, Color.K)
    c2 = Card(Value.VALET, Color.T)
    for v, c in datas:
        try:
            Card(v, c)
        except (ValueError, TypeError) as e:
            print(f"{(v, c) = } {type(e)} ->  {str(e)}")

    print(f"{c1 < c2 = }")
    print(c1)

    # create a deck
    d = Deck()
    print(d)

    # extract X Cards
    X = 7
    h = [d.pop() for _ in range(X)]
    print(h)
    print(d)

    # sort Cards
    h.sort()
    print(h)

    # push all cards fromh to deck
    d.extend(h)
    print(d)

    d += h
    print(d)

    # push again
    d.push(h[0])
    # push a str
    try:
        d.push("toto")
    except (ValueError, TypeError) as e:
        print(f"{type(e)} ->  {str(e)}")

def test_IntEnum():
    class MyInt(enum.IntEnum):
        A=2
        B=enum.auto()
        C=enum.auto()

    print(dir(MyInt))
    print(MyInt.A.__int__(), MyInt.A.name, MyInt.B.value)

if __name__ == '__main__':
    test_card_deck()