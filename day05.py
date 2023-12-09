
class source_destination():

    def __init__(self, destStart, sourceStart, length):
        self.sorceStart = sourceStart
        self.destStart = destStart
        self.length = length

    def mapSource(self, source):
        idxInSource = (source - self.sorceStart)
        if idxInSource < 0 or idxInSource >= self.length:
            return -1
        return self.destStart + idxInSource




class agri_map():

    def parseHeader(self, block):
        txt = block[0].strip().split(' ')[0].split('-')
        self.fromItem = txt[0]
        assert txt[1] == 'to'
        self.toItem = txt[2]

    def parseItems(self, block):
        self.maps = []
        for row in block[1:]:
            rowData = row.strip().split(' ')
            assert len(rowData) == 3
            self.maps.append(source_destination(int(rowData[0]), int(rowData[1]), int(rowData[2])))


    def parse(self, block):
        self.parseHeader(block)
        self.parseItems(block)
        
    def __init__(self, block):
        self.parse(block)

class almanac:
    
    def parseSeeds(self, line):
        l = line.split(':')[1].strip()
        s_seeds = l.split(' ')
        self.seeds = [int(x) for x in s_seeds]


    def parseBlock(self, block):
        self.parseSeeds(block[0])
        runningBlock = []
        self.agri_maps={}
        for line in block[2:]:
            if len(line.strip()) == 0:
                am = agri_map(runningBlock)
                self.agri_maps[am.fromItem]=am
                runningBlock = []
            else:
                runningBlock.append(line)
        if len(runningBlock) > 0 :
            am = agri_map(runningBlock)
            self.agri_maps[am.fromItem]=am

    def __init__(self, block):
        self.parseBlock(block)

