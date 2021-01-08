import re

from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        self.data = [int(i) for i in self.data]
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, adapters):
        adapters = sorted(adapters + [0, max(adapters) + 3])
        differences = [(v - adapters[i - 1]) if i > 0 else 0 for i, v in enumerate(adapters)]
        return differences.count(1) * differences.count(3)

    def __part2(self, adapters):
        adapters = sorted(adapters + [0, max(adapters) + 3])
        differences = "".join([str(v - adapters[i - 1]) if i > 0 else "3" for i, v in enumerate(adapters)])
        d2 = (1 + 1) ** len(re.findall(r"311(?=3)", differences))
        d3 = (1 + 2 + 1) ** len(re.findall(r"3111(?=3)", differences))
        d4 = (3 + 3 + 1) ** len(re.findall(r"31111(?=3)", differences))
        return d2 * d3 * d4
