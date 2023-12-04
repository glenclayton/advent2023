import pytest
import day04

def data():
    return [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]

def test_parse():
    test_data = data()[0]
    no, winners, my = day04.card.parse(test_data)
    assert no == 1
    assert len(winners) == 5 
    assert winners[0] == 41
    assert winners[4] == 17
    assert len(my) == 8
    assert my[0] == 83
    assert my[2] == 6
