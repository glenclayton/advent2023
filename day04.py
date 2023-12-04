
class card:

    @staticmethod
    def parse(line):
        return None,None,None
        
    def __init__(self, line):
        self.num, self.winners, self.yours = card.parse(line)
    
