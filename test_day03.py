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
    assert array[0][0] == 1