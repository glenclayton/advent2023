
def inputToArray(input):
    rv=[]
    for row in input:
        therow = []
        for s in row:
           therow.append(s)
           print(s)
        rv.append(therow)    
    return rv

def isSymbol(s):
    assert s.isdigit() == False
    return s != '.'

class symbol:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class number:
    width = 10
    length = 10
    def addTup(self,tup):
        print(f"trying to add {tup}")
        if tup[0]>=0 and tup[1]>=0 and tup[0]<number.width and tup[1]<number.length:
            self.box[tup]=True

    def boundryBox(self):
        self.box={}
        for i in range(self.x-1,self.xe+2):
            tup=(i,self.y-1)
            self.addTup(tup)
            tup=(i,self.y+1)
            self.addTup(tup)
        tup=(self.x-1,self.y)
        self.addTup(tup)
        tup=(self.xe+1,self.y)
        self.addTup(tup)
            

    def __init__(self,number,x,y):
        self.number=number
        self.x=x
        self.y=y
        self.xe=x+len(str(number))-1
        self.boundryBox()
    
    def borders(self, a_symbol):
        return self.box.get((a_symbol.x,a_symbol.y),False)


def processRow(input,y):
    numbers = []
    symbols = []
    nm = False
    ns = ''
    nstart = -1
    for i in range(0,len(input)):
        s = input[i]
        if s.isdigit():
            if not nm:
                nstart = i
            ns=ns+s
            nm = True
        elif isSymbol(s):
            sym = symbol(i,y)
            symbols.append(sym)
            if nm:
                num = number(int(ns),nstart,y)
                numbers.append(num)
                nm = False
                ns = ''
        elif nm:
            num = number(int(ns),nstart,y)
            numbers.append(num)
            nm = False
            ns = ''
    if nm:
        num = number(int(ns),nstart,y)
        numbers.append(num)

    return symbols, numbers

def processBlock(input):
    number.width = len(input[0].strip())
    number.length = len(input)
    y=0
    symbols = []
    numbers = []
    for line in input:
        s,n = processRow(line.strip(),y)
        symbols = symbols + s
        numbers = numbers + n
        y=y+1
    return symbols, numbers

def findAdjacentNumbers(symbols, numbers):
    rv = []
    for anumber in numbers:
        c = 0
        for asymbol in symbols:
            if anumber.borders(asymbol):
                c = c + 1
        if c == 1:
            rv.append(anumber.number)
            print(f"Part Number {anumber.number}")
    return rv

def findAndSum(input):
    symbols,numbers = processBlock(input)
    partNumbers = findAdjacentNumbers(symbols,numbers)
    dedup = list(dict.fromkeys(partNumbers))
    answer = sum(partNumbers)
    return answer, sum(dedup)

def compute():
    text_file = open("data/input_day03.txt", "r")
    lines = text_file.readlines()
    print(lines)
    print(len(lines))
    text_file.close()
    answer,dd = findAndSum(lines)
    print(f"Day 3 Answer is {answer} or dedups {dd}")

compute()


