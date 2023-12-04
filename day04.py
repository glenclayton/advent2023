
class card:

    @staticmethod
    def parse(line):
        line = line.strip()
        s1 = line.split(":")
        cardno = int(s1[0][4:])
        s2 = s1[1].split('|')
        ws = s2[0][:-1]
    #print(f"A{ws}A")
        ms = s2[1]
        winners = []
        my = []
        for i in range(0,len(ws)//3):
            #print(f"A{ws[i*3:i*3+3]}A")
            winners.append(int(ws[i*3:i*3+3]))
        for i in range(0,len(ms)//3):
            #print(f"A{ms[i*3:i*3+3]}A")
            my.append(int(ms[i*3:i*3+3]))
        return cardno,winners,my
    
    def points(self):
        self.matches = 0
        powe = 0
        for winner in self.winners:
            if winner in self.yours:
                self.matches = self.matches+1
        if self.matches>0:
            powe = pow(2,self.matches-1)
        return powe

    def checkDedup(self):
        dw = list(dict.fromkeys(self.winners))
        dy = list(dict.fromkeys(self.yours))
        a = False
        b = False
        if len(dw) != len(self.winners):
            a = True
        if len(dy) != len(self.yours):
            b = True
        return a,b

    def __init__(self, line):
        self.num, self.winners, self.yours = card.parse(line)

def addToDeck(deck, acard, times=1):
    deck[acard]=deck.get(acard,0)+times

def computeDeck(lines):
    deck = {}
    for line in lines:
        mycard=card(line)
        addToDeck(deck,mycard.num)
        times = deck[mycard.num]
        mycard.points()
        if mycard.matches>0:
            for newcards in range(mycard.num+1, mycard.num+mycard.matches+1):
                print(f"Adding card {newcards} {times}")
                addToDeck(deck,newcards,times)
    print(f"{deck}")
    return sum(deck.values())


def compute():
    text_file = open("data/input_day04.txt", "r")
    lines = text_file.readlines()
    print(lines)
    print(len(lines))
    text_file.close()
    sum=0
    for line in lines:
        mycard=card(line)
        points = mycard.points()
        sum=sum+points
        print(f"{mycard.num}:{sum} {points} | {mycard.winners} | {mycard.yours}")
        a,b = mycard.checkDedup()
        if a or b:
            print(f"card {mycard.num} winner {a} yours {b}")
    print(f"Answer is {sum}")
    decknumber = computeDeck(lines)
    print(f"Part 2 Answer is {decknumber}")

compute()

