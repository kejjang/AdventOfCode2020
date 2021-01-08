from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, questions):
        groups = " ".join(questions).split("  ")
        count = 0
        for g in groups:
            count += len(set(g.replace(" ", "")))
        return count

    def __part2(self, questions):
        groups = " ".join(questions).split("  ")
        count = 0
        for g in groups:
            n = len(g.split(" "))  # number of people in this group
            for i in set(g.replace(" ", "")):  # all question in this group
                count += 1 if g.count(i) == n else 0
        return count
