import random
from individual import Individual


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
        return random.choices(self.individuals, [self.individuals[i].get_score() for i in range(self.size)])[0]

    def random_sample(self):
        return random.choice(self.individuals)

    def breed(self, indiv_a, indiv_b):
        a = indiv_a.get_dna().copy()
        b = indiv_b.get_dna().copy()
        n = len(a)
        left = random.randint(0, n - 2)
        right = random.randint(left + 1, n - 1)
        for i in range(left, right, 1):
            a[i] = a[i] + b[i]
            b[i] = a[i] - b[i]
            a[i] = a[i] - b[i]
        # Chance to mutate here
        if random.randint(0, 100) < 3:
            mutate(a)
            mutate(b)
        self.add_individual(Individual(self.n, a))
        self.add_individual(Individual(self.n, b))


def mutate(arr):
    n = len(arr)
    left = random.randint(0, n - 2)
    right = random.randint(left + 1, n - 1)
    for i in range(left, right, 1):
        arr[i] = n + 1 - arr[i]

