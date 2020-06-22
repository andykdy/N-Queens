from individual import Individual
from population import Population
import math
import time

MAX_GEN = 2500
STAGNANT_THRESHOLD = 0.95


def genetic(n, pop):
    while True:
        population = initialize_pop(n, pop)
        max_iter = MAX_GEN
        perf = []
        while True:
            new_pop = Population(n, pop)
            for i in range(pop):
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
            if len(perf) * performance / sum(perf) > STAGNANT_THRESHOLD and max_iter < MAX_GEN * 0.8:
                print("Evolution stagnant\nRestarting population with increased size\nPop : {0}".format(pop))
                pop += 100
                break
            if max_iter < 0:
                print("Maximum generation reached...\nRetrying with higher population size\n")
                pop += 100
                break
            max_iter -= 1


def initialize_pop(n, pop):
    init_pop = Population(n, pop)
    for i in range(pop):
        init_pop.add_individual(Individual(n))
    return init_pop


def backtrack(n, dna, idx=0):
    filled = n - dna.count(0)
    curr_indiv = Individual(n, dna)
    is_perf = curr_indiv.get_score() == int(filled * (filled - 1) / 2)
    if dna.count(0) == 0 and is_perf:
        print(curr_indiv)
        return True
    for i in range(1, n + 1, 1):
        if is_perf:
            dna[idx] = i
            if backtrack(n, dna, idx + 1):
                return True
            dna[idx] = 0
    return False


def bruteforce(n):
    dna = [1] * n
    max_score = n * (n - 1) / 2
    while True:
        try:
            increment_dna(dna)
        except IndexError:
            print("No solution found for given dimension.\n")
        if 0 not in dna:
            print("Attempting valid DNA {0}".format(dna))
            indiv = Individual(n, dna)
            score = indiv.get_score()
            if score == max_score:
                print(indiv)
                return


def increment_dna(dna):
    dna[-1] += 1
    for i in range(len(dna) - 1, -1, -1):
        if dna[i] > len(dna):
            if i == 0:
                raise IndexError
            dna[i] = 1
            dna[i - 1] += 1


def opt_bruteforce(n):
    dna = [i for i in range(1,n + 1,1)]
    max_score = n * (n - 1) / 2
    while True:
        try:
            optimized_incr(dna)
        except IndexError:
            print("No solution found for given dimension.\n")
        if 0 not in dna:
            print("Attempting valid DNA {0}".format(dna))
            indiv = Individual(n, dna)
            score = indiv.get_score()
            if score == max_score:
                print(indiv)
                return


def optimized_incr(dna):
    while True:
        dna[-1] += 1
        for i in range(len(dna) - 1, -1, -1):
            if dna[i] > len(dna):
                if i == 0:
                    raise IndexError
                dna[i] = 1
                dna[i - 1] += 1
        if len(dna) == len(set(dna)):
            break


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


if __name__ == "__main__":
    n = int_prompt("What dimension (N) would you like to use?\n", 2, 26)
    mode = int_prompt("What mode would you like to use? Input the corresponding number\n0. Genetic Algorithm\n"
                    "1. Backtracking\n2. Brute force\n3. Optimized Brute Force\n", -1, 4)
    init_time = time.perf_counter()
    if mode is 0:
        pop = int_prompt("What population size would you like to use? (Must be even)\n", 4, 1001)
        if pop % 2 is not 0:
            pop += 1
        print("Chosen arguements\nDimension Size:{0}\nPopulation Size:{1}\n".format(n, pop))
        init_time = time.perf_counter()
        genetic(n, pop)
    elif mode is 1:
        backtrack(n, [0 for i in range(n)])
    elif mode is 2:
        bruteforce(n)
    elif mode is 3:
        opt_bruteforce(n)
    end_time = time.perf_counter()
    print("Execution took {0:0.4f} seconds".format(end_time - init_time))
