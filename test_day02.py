import day02

def data():
    test_data= { [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]}
    return test_data

def test_creategame():
    data=test_data()
    line1 = test_data[0]
    game1 = day02.game()
    game1.parseLine(line1)
    pulls1 = game1.pulls
    for pull in pulls1:
        assert pull['blue'] == 3
        assert pull['red'] == 4

