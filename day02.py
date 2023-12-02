import re

class game:
    def __init__(self,num):
        self.pulls = []
        self.num = num

    @staticmethod
    def parse_text(input_text):
        match = re.match(r'(\d+)\s+(.+)', input_text)
    
        if match:
           # Extract the numeric and non-numeric parts
          quantity = int(match.group(1))
          item = match.group(2)
        
          # Return the result as a tuple
        return quantity, item

    def parseLine(self,line):
        print(f"line ={line}")
        tokens = line.split(': ')
        games = tokens[1].split('; ')
        for thegame in games:
            cubes = thegame.split(', ')
            pull={}
            for cube in cubes:
                print(f"cube = {cube}")
                (num, colour) = game.parse_text(cube)
                pull[colour]=num
            self.pulls.append(pull)

    def checkPossible(self,r,g,b):
        rv = True
        for pull in self.pulls:
            br = pull.get('red',0)
            bb = pull.get('blue',0)
            bg = pull.get('green',0)
            possible = (br<=r) and (bb<=b) and (bg<=g)
            rv = rv and possible
        return rv


games=[]

text_file = open("data/input_day02.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()

c=1
sum=0
for line in lines:
    thegame=game(c)
    thegame.parseLine(line)
    rv = thegame.checkPossible(12,13,14)
    if rv:
        sum=sum+c
    print(f"Game {c} possible is {rv}")
    c=c+1

print(f"Answer={sum}")
