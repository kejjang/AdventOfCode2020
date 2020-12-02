import math

from itertools import combinations
from utilities.operator import Base


class Operator(Base):
    def exec(self, entries):
        for item in combinations(self.data, entries):
            if sum(item) == 2020:
                return math.prod(item)
