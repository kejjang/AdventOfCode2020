import math

from itertools import combinations
from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, entries):
        for item in combinations(self.data, entries):
            if sum(item) == 2020:
                return math.prod(item)
