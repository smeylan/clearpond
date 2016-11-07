import pandas

class NeighborhoodDictionary(object):
    def __init__(self, cp_path):
        self.table = pandas.read_table(cp_path, header=None)
        words = [x.lower() for x in self.table.loc[:,0]]
        self.orthNeighbors = dict(zip(words, [str(x).lower().split(';') for x in self.table.loc[:,7]]))
        self.phoneNeighbors = dict(zip(words, [str(x).lower().split(';') for x in self.table.loc[:,31]]))
