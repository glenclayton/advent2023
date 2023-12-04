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
    ],[8,2,2,1,0,0]

@pytest.mark.skip
def test_parse():
    dat,_ = data()
    test_data = dat[0]
    no, winners, my = day04.card.parse(test_data)
    assert no == 1
    assert len(winners) == 5 
    assert winners[0] == 41
    assert winners[4] == 17
    assert len(my) == 8
    assert my[0] == 83
    assert my[2] == 6

@pytest.mark.skip
def test_pow_single():
    dat,_ = data()
    test_data = dat[0]
    mycard = day04.card(test_data)
    assert mycard.points() == 8

@pytest.mark.skip
def test_pow_multiplie():
    dat, ans = data()
    rsum = 0
    for l,a in zip(dat, ans):
        mycard = day04.card(l)
        assert mycard.points() == a
        rsum = rsum+mycard.points()
    assert rsum == 13

@pytest.mark.skip
def test_real():
    test_data = "Card   1: 99 65 21  4 72 20 77 98 27 70 | 34 84 74 18 41 45 72  2  1 75 52 47 50 93 25 10 79 87 42 69  8 12 54 96 92"
    mycard = day04.card(test_data)
    assert mycard.winners[0] == 99
    assert mycard.winners[9] == 70
    assert mycard.yours[0] == 34
    assert mycard.yours[7] == 2
    assert mycard.yours[8] == 1
    assert mycard.yours[24] == 92
    assert mycard.yours[20] == 8
    assert mycard.points() == 1

@pytest.mark.skip
def test_real2():
    test_data = "Card  49:  8 24 35 89 29 80 42 90 79 41 | 16 60 95 58 53  8 55 22 65 15 97 74 64 93 82 51  1 78 73 61 98 23  5  7 37"
    mycard = day04.card(test_data)
    assert len(mycard.winners) == 10

@pytest.mark.skip
def test_cardsdeck():
    dat, ans = data()
    rsum = day04.computeDeck(dat)
    assert rsum == 30