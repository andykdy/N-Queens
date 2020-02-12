import random
from functools import reduce


class State:
    def __init__(self,N):
        self.N = N
        self.DNA = [random.randint(1,self.N) for i in range(self.N)]

    def print(self):
        res = self.DNA
        print_line(self.N)
        for i in range(self.N):
            for j, val in enumerate(res):
                if i + 1 == val:
                    print("|QN",end="")
                else:
                    print("|  ",end="")
            print("|")
            print_line(self.N)

    def get_score(self):
        score = 0
        # Vertical hits are not possible because each queen owns one column
        score += check_horizontal(self.DNA)
        score += check_diagonal(self.DNA)
        print("State has a score of {0}".format(score))
        return score


def check_horizontal(position):
    score = 0
    for x, y in enumerate(position):
        score += reduce(lambda sum, curr: sum + 1 if curr == y else sum, [0] + position)
    # Remove self hits
    score -= len(position)
    return score


def check_diagonal(position):
    score = 0
    for x1, y1 in enumerate(position):
        for x2, y2 in enumerate(position):
            if abs(x1 - x2) == abs(y1 - y2):
                score+=1
    # Remove self hits
    score -= len(position)
    return score
    return 0


def print_line(N):
    for i in range(N):
        print(".--", end="")
    print(".")
