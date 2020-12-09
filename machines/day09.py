from itertools import combinations
from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        self.data = [int(i) for i in self.data]
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self, with_key=False):
        for idx in range(25, len(self.data)):
            if not self.__is_valid_xmas_item(idx):
                return [idx, self.data[idx]] if with_key else self.data[idx]

    def __part2(self):
        weak_idx, weak_number = self.__part1(with_key=True)
        while 1:
            for n in range(2, weak_idx + 1):
                for start in range(0, weak_idx - n + 1):
                    if sum(item := self.data[start : start + n]) == weak_number:
                        return sum((sorted(item) * 2)[n - 1 : n + 1])

    def __is_valid_xmas_item(self, i):
        for item in combinations(self.data[i - 25 : i], 2):
            if self.data[i] == sum(item):
                return True
        return False
