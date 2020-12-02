import math

from itertools import combinations
from utilities.operator import Base


class Operator(Base):
    def load_data(self, day_num):
        super().load_data(day_num=day_num)
        self.data = [int(item) for item in self.data]

    def exec(self, entries):
        for item in combinations(self.data, entries):
            if sum(item) == 2020:
                return math.prod(item)
