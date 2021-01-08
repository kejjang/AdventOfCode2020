from collections import defaultdict
from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        self.__starting_numbers = [int(i) for i in self.data[0].split(",")]
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        return self.__play(2020)

    def __part2(self) -> int:
        return self.__play(30000000)

    def __play(self, turns):
        turn_records = defaultdict(list)
        this_turn = None

        for turn_idx, value in enumerate(self.__starting_numbers):
            turn_records[value] += [turn_idx]
            this_turn = value

        for turn_idx in range(len(self.__starting_numbers), turns):
            this_turn = 0 if len(turn_records[this_turn]) == 1 else turn_records[this_turn][-1] - turn_records[this_turn][-2]
            turn_records[this_turn] += [turn_idx]

        return this_turn
