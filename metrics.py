class Metrics:
    def __init__(self):
        self.nfe = 0

    def evaluate(self, ind, fitness):
        self.nfe += 1
        return fitness(ind)
