import random
import math
from functools import reduce



"""
    An individual in a population
    n = number of queen pieces and dimensional width of board
    score = fitness of the individual
    DNA = a list of integers where the index is the x coord and the value is the y coord
    @@@ DNA can be improved by always generating a random but unique DNA with no repeating values
    @@@ Maybe present "number of placed pieces" as a private variable?
"""
class Individual:
    def __init__(self, n, manual_dna=None):
        self.n = n
        self.score = -1
        if manual_dna is None:
            self.DNA = random.sample([i + 1 for i in range(n)], n)
        else:
            self.DNA = manual_dna

    def __str__(self):
        ret = print_line(self.n, "")
        for i in range(self.n):
            for j, val in enumerate(self.DNA):
                ret = ret + "|QN" if i + 1 == val else ret + "|  "
            ret += "|\n"
            ret = print_line(self.n, ret)
        return ret
    """
        Calculate the score by checking the horizontal and diagonal conflict.
        Note:   Vertical conflicts are not possible because each queen owns a column
        @@@ Some checks are redundant... I can reduce a N * N check into N + (N - 1) check
        @@@ Wondering if self.score - combin is needed... 
    """
    def get_score(self):
        if self.score is - 1:
            placed = self.n - self.DNA.count(0)
            combin = int(placed * (placed - 1) / 2)
            self.score = 0
            self.score += check_diagonal(self.DNA)
        return self.score

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
    n = len(position) - position.count(0)
    score = n * (n - 1) / 2 + n
    seen = []
    for x1, y1 in enumerate(position):
        for x2, y2 in enumerate(position):
            if seen.count(x2) is 0:
                if abs(x1 - x2) == abs(y1 - y2) and y1 * y2 is not 0:
                    score -= 1
        seen.append(x1)
    return score


"""
    Util for printing an individual
"""
def print_line(n, val):
    for i in range(n):
        val += ".--"
    return val + ".\n"
