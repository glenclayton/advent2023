
def inputToArray(input):
    rv=[]
    for row in input:
        therow = []
        for s in row:
           therow.append(s)
           print(s)
        rv.append(therow)    
    return rv

