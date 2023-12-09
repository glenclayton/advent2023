
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
    def __init__(self):
        return

