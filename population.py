import random
from individual import Individual

# Mutate chance in percentage
MUTATE_CHANCE = 0

"""
    An population of individuals
    n = number of queen pieces and dimensional width of board
    size = number of individuals in this population
    fitness_total = the sum of fitness for each individual in the population
    individuals = a list of individuals 
    @@@ breed() shouldn't be implemented to add two new Individuals. What if the user wants an odd numbered population?
"""
class Population:
    def __init__(self, n, size):
        self.n = n
        self.size = size
        self.fitness_total = None
        self.individuals = []

    def get_fitness(self):
        if self.fitness_total is None:
            self.fitness_total = calc_fitness_total(self.individuals, self.size)
        return self.fitness_total

    def add_individual(self, i):
        self.individuals.append(i)

    """ Returns an individual. Weighted sampling based on fitness(score) of the individual
        Higher fitness == higher chance of selection
    """
    def weighted_sample(self):
        return random.choices(self.individuals, [self.individuals[i].get_score() for i in range(self.size)])[0]

    """ Returns an individual. Random sampling based on no criteria
        All individuals have equal chance of selection
    """
    def random_sample(self):
        return random.choice(self.individuals)

    """ Returns an individual. Selected via index
        Primarily used for testing 
    """
    def index_sample(self, idx):
        return self.individuals[idx]

    """ Breeds two given individuals via randomly swapping numbers within a certain slice"""
    def breed(self, indiv_a, indiv_b, is_mutate=True):
        a = indiv_a.get_dna().copy()
        b = indiv_b.get_dna().copy()
        n = len(a)
        left = random.randint(0, n - 2)
        right = random.randint(left + 1, n - 1)
        ret = [0] * (right - left)
        for i in range(left, right, 1):
            ret[i - left] = a[left]
            a.remove(a[left])
        ret = ret + random.sample(a, n - right + left)
        # Chance to mutate here
        if random.randint(0, 100) < MUTATE_CHANCE and is_mutate:
            mutate(a)
            mutate(b)
        self.add_individual(Individual(self.n, ret))


def mutate(arr):
    n = len(arr)
    left = random.randint(0, n - 2)
    right = random.randint(left + 1, n - 1)
    for i in range(left, right, 1):
        arr[i] = n + 1 - arr[i]


def calc_fitness_total(individuals, n):
    return sum([individuals[i].get_score() for i in range(n)])
