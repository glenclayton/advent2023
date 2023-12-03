
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
    return s in '$*#'

class symbol:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class number:
    def __init__(self,number,x,y):
        self.number=number
        self.x=x
        self.y=y
        self.xe=x+len(str(number))-1


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

