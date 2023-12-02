import day02
import pytest

def data():
    test_data= { "data" : [
    {"s": "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "p":True,"pow":48},
    {"s":"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue","p" : True,"pow":12},
    {"s":"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red","p" : False,"pow":1560},
    {"s":"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red","p" : False,"pow":630},
    {"s":"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green","p":True,"pow":36}]}
    return test_data

@pytest.mark.skip
def test_parse():
    (num, colour) = day02.game.parse_text('2 blue')
    assert num == 2
    assert colour == 'blue'
    (num, colour) = day02.game.parse_text('12 red')
    assert num == 12
    assert colour == 'red'

@pytest.mark.skip
def test_creategame():
    test_data=data()
    line1 = test_data['data'][0]['s']
    game1 = day02.game(0)
    assert game1.num == 0
    game1.parseLine(line1)
    pulls1 = game1.pulls
    print(pulls1)
    pull=pulls1[0]
    print(f"pull={pull}")
    assert pull['blue'] == 3
    assert pull['red'] == 4
    pull=pulls1[1]
    print(f"pull={pull}")
    assert pull['green'] == 2
    assert pull['blue'] == 6

@pytest.mark.skip
def test_checkgame():
    test_data=data()
    for line in test_data['data']:
        line1 = line['s']
        p1 = line['p']
        thegame=day02.game(0)
        thegame.parseLine(line1)
        rv = thegame.checkPossible(12,13,14)
        assert rv == p1

@pytest.mark.skip
def test_powgame():
    test_data=data()
    for line in test_data['data']:
        line1 = line['s']
        p1 = line['p']
        pow1 = line['pow']
        thegame=day02.game(0)
        thegame.parseLine(line1)
        rv = thegame.minimumPower()
        assert rv == pow1