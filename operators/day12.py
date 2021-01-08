from typing import List
from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        self.__move = {"N": [0, -1], "S": [0, 1], "E": [1, 0], "W": [-1, 0]}
        self.__turn = {"L": ["N", "W", "S", "E"], "R": ["N", "E", "S", "W"]}
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, instructions: List[str]) -> int:
        location = [0, 0]
        facing = "E"
        for item in instructions:
            inst_type, value = item[0], int(item[1:])
            if inst_type in self.__move:
                target = [i * value for i in self.__move[inst_type]]
                location = list(map(sum, zip(location, target)))
            elif inst_type == "F":
                target = [i * value for i in self.__move[facing]]
                location = list(map(sum, zip(location, target)))
            elif inst_type in self.__turn:
                diff = value // 90
                facing = self.__turn[inst_type][(self.__turn[inst_type].index(facing) + diff) % 4]
        return sum([abs(i) for i in location])

    def __part2(self, instructions: List[str]) -> int:
        location = [0, 0]
        waypoint = [10, -1]
        for item in instructions:
            inst_type, value = item[0], int(item[1:])
            if inst_type in self.__move:
                target = [i * value for i in self.__move[inst_type]]
                waypoint = list(map(sum, zip(waypoint, target)))
            elif inst_type == "F":
                target = [i * value for i in waypoint]
                location = list(map(sum, zip(location, target)))
            elif inst_type in self.__turn:
                diff = value // 90
                direction1 = self.__turn[inst_type][(self.__turn[inst_type].index("W" if waypoint[0] < 0 else "E") + diff) % 4]
                direction2 = self.__turn[inst_type][(self.__turn[inst_type].index("N" if waypoint[1] < 0 else "S") + diff) % 4]
                if direction1 in ["E", "W"]:
                    waypoint = [abs(waypoint[0]) * sum(self.__move[direction1]), abs(waypoint[1]) * sum(self.__move[direction2])]
                else:  # direction2 in ["E", "W"]
                    waypoint = [abs(waypoint[1]) * sum(self.__move[direction2]), abs(waypoint[0]) * sum(self.__move[direction1])]
        return sum([abs(i) for i in location])
