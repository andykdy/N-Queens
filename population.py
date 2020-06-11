import random


class Population:
    def __init__(self, n, size):
        self.n = n
        self.size = size
        self.fitness_total = None
        self.individuals = []

    def get_fitness(self):
        if self.fitness_total is None:
            self.calc_fitness_total()
        return self.fitness_total

    def add_individual(self, i):
        self.individuals.append(i)

    def calc_fitness_total(self):
        self.fitness_total = sum([self.individuals[i].get_score() for i in range(self.size)])

    def weighted_sample(self):
        weighted = []
        for i, ind in enumerate(self.individuals):
            for j in range(ind.get_score()):
                weighted.append(i)
        return self.individuals[random.choice(weighted)]


