import math

from itertools import combinations
from utilities.data import PuzzleInput


class Operator:
    def __init__(self, autoload_data=True):
        if autoload_data:
            self.load_data(1)

    def load_data(self, day_num):
        self.data = [int(item) for item in PuzzleInput.get(day_num)]

    def exec(self, entries):
        for item in combinations(self.data, entries):
            if sum(item) == 2020:
                return math.prod(item)
