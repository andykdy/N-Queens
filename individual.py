import random
from functools import reduce

""" An individual in a population. """


class Individual:
    def __init__(self, n, manual_dna=None):
        self.n = n
        self.DNA = [random.randint(1, self.n) for i in range(self.n)] if manual_dna is None else manual_dna
        self.score = 0

    def __str__(self):
        ret = print_line(self.n, "")
        for i in range(self.n):
            for j, val in enumerate(self.DNA):
                ret = ret + "|QN" if i + 1 == val else ret + "|  "
            ret += "|\n"
            ret = print_line(self.n, ret)
        return ret

    def get_score(self):
        combin = int(self.n * (self.n - 1) / 2)
        if self.score is 0:
            # Vertical hits are not possible because each queen owns one column
            self.score += check_horizontal(self.DNA)
            self.score += check_diagonal(self.DNA)
            self.score = int(self.score / 2)
        return self.score - combin

    def get_dna(self):
        return self.DNA


def check_horizontal(position):
    n = len(position) - 1
    score = n * (1 + n) + n + 1
    for x, y in enumerate(position):
        score -= reduce(lambda _sum, curr: _sum + 1 if curr == y else _sum, [0] + position)
    return score


def check_diagonal(position):
    # TODO More optimal algorithm possible
    n = len(position) - 1
    score = n * (1 + n) + n + 1
    for x1, y1 in enumerate(position):
        for x2, y2 in enumerate(position):
            if abs(x1 - x2) == abs(y1 - y2):
                score -= 1
    return score


def print_line(n, val):
    for i in range(n):
        val += ".--"
    return val + ".\n"
