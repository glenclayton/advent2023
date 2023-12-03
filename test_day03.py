import day03

def data():
    test_data= [
        "467..114..\n",
        "...*......\n",
        "..35..633.\n",
        "......#...\n",
        "617*......\n",
        ".....+.58.\n",
        "..592.....\n",
        "......755.\n",
        "...$.*....\n",
        ".664.598..\n"
    ]
    return test_data

def data2():
    return [
        "12.......*..",
        "+.........34",
        ".......-12..",
        "..78........",
        "..*....60...",
        "78.........9",
        ".5.....23..$",
        "8...90*12...",
        "............",
        "2.2......12.",
        ".*.........*",
        "1.1..503+.56"]

def test_inputToArray():
    test_data=['12','34']
    array = day03.inputToArray(test_data)
    assert array[0][0] == '1'
    assert array[0][1] == '2'
    assert array[1][0] == '3'
    assert array[1][1] == '4'

def test_isSymbol():
    assert day03.isSymbol('$') == True
    assert day03.isSymbol('.') == False

def test_processRowSymbols():
    test_data = '..$.*.#'
    symbols, _ = day03.processRow(test_data,0)
    assert len(symbols) == 3
    assert symbols[0].x == 2
    assert symbols[0].y == 0

def test_processRowNumbers():
    test_data = '1'
    _, numbers = day03.processRow(test_data,0)
    assert numbers[0].number == 1
    test_data = '12'
    _, numbers = day03.processRow(test_data,0)
    assert numbers[0].number == 12
    test_data = '.12.'
    _, numbers = day03.processRow(test_data,0)
    assert numbers[0].number == 12
    assert numbers[0].x == 1
    test_data = '.12.34'
    _, numbers = day03.processRow(test_data,0)
    assert len(numbers) == 2
    assert numbers[0].number == 12
    assert numbers[0].x == 1
    assert numbers[1].number == 34
    assert numbers[1].x == 4
    test_data = '.12$34'
    _, numbers = day03.processRow(test_data,0)
    assert len(numbers) == 2
    assert numbers[0].number == 12
    assert numbers[0].x == 1
    assert numbers[1].number == 34
    assert numbers[1].x == 4
    test_data = '34$'
    _, numbers = day03.processRow(test_data,0)
    assert len(numbers) == 1
    assert numbers[0].number == 34
    assert numbers[0].x == 0
    test_data = '..34'
    _, numbers = day03.processRow(test_data,0)
    assert len(numbers) == 1
    assert numbers[0].number == 34
    assert numbers[0].x == 2

def test_boundayBox():
    agame = day03.number(123,0,0)
    assert len(agame.box) == 5
    assert agame.box[(0,1)] == True
    assert agame.box.get((4,0)) == None
    assert agame.box[(3,0)] == True
    agame = day03.number(1,1,1)
    assert len(agame.box) == 8
    assert agame.box.get((1,1)) == None
    assert agame.box.get((0,0)) ==True
    assert agame.box.get((2,2)) ==True
    assert agame.box.get((0,1)) ==True
    assert agame.box.get((2,1)) ==True
    agame= day03.number(789,7,1)
    assert len(agame.box) == 9
    assert agame.box.get((6,1)) ==True
    assert agame.box.get((6,0)) ==True
    assert agame.box.get((6,2)) ==True
    assert agame.box.get((7,2)) ==True

def test_block():
    test_data=data()
    answer,dd = day03.findAndSum(test_data)
    assert answer == 4361

def test_block2():
    test_data=data2()
    answer, dd = day03.findAndSum(test_data)
    assert answer == 925

def test_findGearSymbols():
    test_data = '..*.*.'
    symbols, _ = day03.processRow(test_data,0)
    gears = day03.findGearSymbols(symbols)
    assert len(gears) == 2
    assert gears[0].x == 2
    assert gears[1].x == 4

def test_gears():
    test_data = data()
    symbols, numbers = day03.processBlock(test_data)
    ans = day03.findGears(symbols, numbers)
    assert ans == 467835