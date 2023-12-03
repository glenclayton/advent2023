import day03

def data():
    test_data= [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
    return test_data

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