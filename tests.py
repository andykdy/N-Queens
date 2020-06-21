import unittest
from individual import Individual
from population import Population


class TestIndividuals(unittest.TestCase):

    def test_horizontal(self):
        a = Individual(5, [1, 1, 1, 1, 1])
        self.assertEqual(a.get_score(), 0)

    def test_diagonal(self):
        a = Individual(5, [1, 2, 3, 4, 5])
        self.assertEqual(a.get_score(), 0)

    def test_perfect_four(self):
        a = Individual(4, [2, 4, 1, 3])
        self.assertEqual(a.get_score(), 6)

    def test_perfect_six(self):
        a = Individual(6, [2, 4, 6, 1, 3, 5])
        self.assertEqual(a.get_score(), 15)

    def test_norm(self):
        a = Individual(4, [1, 1, 3, 3])
        self.assertEqual(a.get_score(), 2)

    # Max conflict is (2 * 1)/2 == 1
    # With one conflict, this max is reached. Thus a score of 0
    def test_partial_conflict(self):
        a = Individual(4, [1, 1, 0, 0])
        self.assertEqual(a.get_score(), 0)

    def test_partial_perfect(self):
        a = Individual(4, [1, 0, 2, 0])
        self.assertEqual(a.get_score(), 1)

    def test_indiv_add(self):
        n = 5
        a = Individual(n, [1, 1, 1, 1, 1])
        b = Individual(n, [5, 5, 5, 5, 5])
        pop = Population(n, 2)
        self.assertEqual(len(pop.individuals), 0)
        pop.add_individual(a)
        self.assertEqual(len(pop.individuals), 1)
        pop.add_individual(b)
        self.assertEqual(len(pop.individuals), 2)

    def test_breed(self):
        n = 5
        a = Individual(n, [1, 1, 1, 1, 1])
        b = Individual(n, [5, 5, 5, 5, 5])
        pop = Population(n, 2)
        pop.breed(a, b, 1, 3)
        self.assertEqual(pop.index_sample(0).get_dna(), [1, 5, 5, 1, 1])
        self.assertEqual(pop.index_sample(1).get_dna(), [5, 1, 1, 5, 5])

    def test_total_fitness_1(self):
        n = 5
        a = Individual(n, [1, 1, 1, 1, 1])
        b = Individual(n, [5, 5, 5, 5, 5])
        pop = Population(n, 2)
        pop.add_individual(a)
        pop.add_individual(b)
        self.assertEqual(pop.get_fitness(), 0)

    def test_total_fitness_2(self):
        n = 4
        a = Individual(n, [2, 4, 1, 3])
        b = Individual(n, [3, 1, 4, 2])
        pop = Population(n, 2)
        pop.add_individual(a)
        pop.add_individual(b)
        self.assertEqual(pop.get_fitness(), 12)




if __name__ == '__main__':
    unittest.main()
