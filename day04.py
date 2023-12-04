
class card:

    @staticmethod
    def parse(line):
        line = line.strip()
        s1 = line.split(":")
        cardno = int(s1[0][4:])
        s2 = s1[1].split('|')
        ws = ' '+s2[0].strip()
        print(f"A{ws}A")
        ms = s2[1]
        winners = []
        my = []
        for i in range(0,len(ws)//3):
            print(f"A{ws[i*3:i*3+3]}A")
            winners.append(int(ws[i*3:i*3+3]))
        for i in range(0,len(ms)//3):
            print(f"A{ms[i*3:i*3+3]}A")
            my.append(int(ms[i*3:i*3+3]))
        return cardno,winners,my
        
    def __init__(self, line):
        self.num, self.winners, self.yours = card.parse(line)
    
