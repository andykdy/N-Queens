from individual import Individual
from population import Population


def main(n, pop):
    init_pop = Population(n, pop)
    for i in range(pop):
        init_pop.add_individual(Individual(n))
    population = init_pop
    running = True
    while running:
        new_pop = Population(n, pop)
        for i in range(pop):
            ind_a = population.weighted_sample()
            ind_b = population.weighted_sample()
            new_pop.breed(ind_a, ind_b)
        print(new_pop.get_fitness())


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
    n = int_prompt("What dimension would you like to use?\n", 1, 10)
    pop = int_prompt("What population size would you like to use?\n", 1, 1001)
    print("Chosen arguements\nDimension Size:{0}\nPopulation Size:{1}".format(n, pop))
    main(n, pop)
