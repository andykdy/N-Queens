from individual import Individual


def test(n,pop):
    population = {}
    for i in range(pop):
        new_pop = Individual(n)
        # print(new_pop.concat_dna())
        # population[new_pop] = new_pop.get_score()
        print (new_pop)
    pass

def main(n):
    new_state = Individual(n)
    new_state.print()
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
    n = int_prompt("What dimension would you like to use?\n", 0, 10)
    pop = int_prompt("What population size would you like to use?\n", 0, 1001)
    print("Chosen arguements\nDimension Size:{0}\nPopulation Size:{1}".format(n,pop))
    test(n, pop)
    #main(n_val, pop)
