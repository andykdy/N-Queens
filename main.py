from individual import Individual
from population import Population
import math

MAX_GEN = 2500
STAGNANT_THRESHOLD = 0.95


def main(n, pop):
    while True:
        population = initialize_pop(n, pop)
        max_iter = MAX_GEN
        perf = []
        while True:
            new_pop = Population(n, pop)
            for i in range(math.ceil(pop/2)):
                ind_a = population.weighted_sample()
                ind_b = population.weighted_sample()
                new_pop.breed(ind_a, ind_b)
            population = new_pop
            performance = population.get_fitness() / pop
            perf.append(performance)
            print("Generation {0:0>4d} | Performance {1:.2f}".format(MAX_GEN - max_iter, performance))
            best = max(population.individuals, key=lambda x: x.get_score())
            if best.get_score() == n * (n - 1) / 2:
                print("Found optimal solution...\n {0}".format(best))
                return
            if len(perf) * performance / sum(perf) > STAGNANT_THRESHOLD and max_iter < MAX_GEN * 0.6:
                print("Evolution stagnant\nRestarting population with increased size\n")
                pop += 100
                break
            if max_iter < 0:
                print("Maximum generation reached...\nRetrying with higher population size\n")
                pop += 100
                break
            max_iter -= 1


def int_prompt(question, rmin, rmax):
    while True:
        int_val = input(question)
        try:
            int_val = int(int_val)
            if int_val <= rmin or int_val >= rmax:
                raise TypeError
            return int_val
        except TypeError:
            print("N value must be between {0} and {1}\nTry Again\n".format(rmin, rmax))
        except ValueError:
            print("N value must be an integer\nTry Again\n")


def initialize_pop(n, pop):
    init_pop = Population(n, pop)
    for i in range(pop):
        init_pop.add_individual(Individual(n))
    return init_pop


if __name__ == "__main__":
    n = int_prompt("What dimension would you like to use?\n", 1, 26)
    pop = int_prompt("What population size would you like to use? (Must be even)\n", 4, 1001)
    if pop % 2 is not 0:
        pop += 1
    print("Chosen arguements\nDimension Size:{0}\nPopulation Size:{1}".format(n, pop))
    main(n, pop)
