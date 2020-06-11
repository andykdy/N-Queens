import random
import math
from functools import reduce

"""
A individual in a population.
"""


class Individual:
    def __init__(self, n, manual_dna=None):
        self.n = n
        self.DNA = [random.randint(1, self.n) for i in range(self.n)] if manual_dna is None else manual_dna
        self.score = 0

    # Required to use class as Key in dictionary
    def __hash__(self):
        return hash(self.concat_dna())

    def __str__(self):
        ret = print_line(self.n, "")
        for i in range(self.n):
            for j, val in enumerate(self.DNA):
                ret = ret + "|QN" if i + 1 == val else ret + "|  "
            ret += "|\n"
            ret = print_line(self.n, ret)
        return ret

    def get_score(self):
        if self.score is 0:
            # Vertical hits are not possible because each queen owns one column
            self.score += check_horizontal(self.DNA)
            self.score += check_diagonal(self.DNA)
            self.score = int(self.score / 2)
            print("Individual has a score of {0}".format(self.score))
        return self.score

    def concat_dna(self):
        ret = 0
        for i in range(self.n - 1, -1, -1):
            ret += (math.pow(10, i) * self.DNA[self.n - i - 1])
        return int(ret)


def check_horizontal(position):
    score = -len(position)
    for x, y in enumerate(position):
        score += reduce(lambda _sum, curr: _sum + 1 if curr == y else _sum, [0] + position)
    return score


def check_diagonal(position):
    # TODO More optimal algorithm possible
    score = - len(position)
    for x1, y1 in enumerate(position):
        for x2, y2 in enumerate(position):
            if abs(x1 - x2) == abs(y1 - y2):
                score += 1
    return score


def print_line(n, val):
    for i in range(n):
        val += ".--"
    return val + ".\n"
