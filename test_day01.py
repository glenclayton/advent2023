import day01

def test_day01():
    data = [
    ("two1nine",29),
    ("eightwothree",83),
    ("abcone2threexyz",13),
    ("xtwone3four",24),
    ("4nineeightseven2",42),
    ("zoneight234",14),
    ("7pqrstsixteen",76),
    ("x1x2x3",13),
    ("xone",11),
    ("nineeightsevensixfivefourthreetwoone",91),
    ("eighthree",83),
    ("sevenine",79),
    ("eightwone7",87)]
    for tdat in data:
        rv=day01.find_number(day01.replace_text(tdat[0]))
        assert(rv == tdat[1])

