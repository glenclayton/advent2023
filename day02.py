import re

class game:
    def __init__(self):
        self.pulls = []
    
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
            


games=[]

text_file = open("data/input_day02.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()


