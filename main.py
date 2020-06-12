from individual import Individual
from population import Population


def test(n, pop):
    population = Population(n, pop)
    for i in range(pop):
        population.add_individual(Individual(n))

    new_pop = Population(n,pop)
    for i in range(pop):
        ind_a = population.weighted_sample()
        ind_b = population.weighted_sample()
        new_pop.breed(ind_a,ind_b)
    print(population.weighted_sample())



def main(n):
    new_state = Individual(n)
    new_state.get_score()


def int_prompt(question, min, max):
    while True:
        int_val = input(question)
        try:
            int_val = int(int_val)
            if int_val <= min or int_val >= max:
                raise TypeError
            return int_val
        except TypeError:
            print("N value must be between {0} and {1}\nTry Again\n".format(min, max))
        except ValueError:
            print("N value must be an integer\nTry Again\n")



if __name__ == "__main__":
    n = int_prompt("What dimension would you like to use?\n", 1, 10)
    pop = int_prompt("What population size would you like to use?\n", 1, 1001)
    print("Chosen arguements\nDimension Size:{0}\nPopulation Size:{1}".format(n,pop))
    test(n, pop)
    #main(n_val, pop)
