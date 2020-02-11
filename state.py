import random
from functools import reduce


class State:
    def __init__(self,N):
        self.N = N
        self.DNA = [random.randint(1,self.N) for i in range(self.N)]

    def print(self):
        res = self.DNA
        print(self.DNA)
        print_line(self.N)
        for i in range(self.N):
            for j, val in enumerate(res):
                if i + 1 == val:
                    print("|QN",end="")
                else:
                    print("|  ",end="")
            print("|")
            print_line(self.N)


def print_line(N):
    for i in range(N):
        print(".--", end="")
    print(".")
