import random
from functools import reduce

""" An individual in a population. """


class Individual:
    def __init__(self, n, manual_dna=None):
        self.n = n
        self.score = 0
        if manual_dna is None:
            self.DNA = [random.randint(1, self.n) for i in range(self.n)]
            self.placed = n
        else:
            self.DNA = manual_dna
            self.placed = n - self.DNA.count(0)

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

"""
    Input : dna (position of chess pieces on the board)
    Output: int

    0 means that there are no horizontal conflicts
    Maximum value is n * (n - 1) / 2 meaning all n pieces are lined up horizontally
"""
def check_horizontal(dna):
    n = len(dna) - dna.count(0)
    score = n * (n - 1) + n
    for x, y in enumerate(dna):
        # append dna to [0] for reduction
        score -= reduce(lambda _sum, curr: _sum + 1 if curr == y and curr is not 0 else _sum, [0] + dna)
    return score

"""
    Input : dna (position of chess pieces on the board)
    Output: int

    0 means that there are no diagonal conflicts
    Maximum value is n * (n - 1) / 2 meaning all n pieces are lined up diagonally
"""
def check_diagonal(position):
    # TODO More optimal algorithm possible
    n = len(position) - position.count(0) - 1
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
