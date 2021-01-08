import re

from math import prod
from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        return self.__solve("in_order")

    def __part2(self) -> int:
        return self.__solve("add_first")

    def __solve(self, solve_type="in_order"):
        func = self.__solve_add_first if solve_type == "add_first" else self.__solve_in_order
        answers = []
        pattern = r"(\([\d\+\*]*?\))"
        for q in self.data:
            q = q.replace(" ", "")
            while 1:
                match = re.findall(pattern, q)
                if len(match) > 0:
                    for m in match:
                        q = q.replace(m, str(func(m[1:-1])))
                else:
                    break
            answers += [func(q)]
        return sum(answers)

    def __solve_in_order(self, q):
        numbers = [int(i) for i in re.split(r"[\+\*]", q)]
        operators = re.split(r"\d+?", q)[1:-1]

        result = numbers.pop(0)
        for o in operators:
            if o == "+":
                result += numbers.pop(0)
            elif o == "*":
                result *= numbers.pop(0)

        return result

    def __solve_add_first(self, q):
        segs = q.split("*")
        for idx, val in enumerate(segs):
            if val.count("+") > 0:
                segs[idx] = sum([int(i) for i in val.split("+")])
            else:
                segs[idx] = int(val)

        return prod(segs)
