import copy

from typing import List, Dict
from utilities.operator import OperatorBase


class Operator(OperatorBase):
    __accumulator = 0
    __ran = []
    __p = 0
    __terminated = False

    def exec(self, part: int = 1):
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, instructions_raw_data: List[str]):
        instructions = self.__instruction_parser(instructions_raw_data)
        self.__boot(instructions)
        return self.__accumulator

    def __part2(self, instructions_raw_data: List[str]):
        instructions = self.__instruction_parser(instructions_raw_data)
        test_cases = self.__build_test_case(instructions)

        for case in test_cases:
            self.__reset()
            if self.__boot(case):
                return self.__accumulator
        return False

    def __instruction_parser(self, instructions_raw_data: List[str]):
        instructions = []
        for inst in instructions_raw_data:
            op, arg = inst.strip().split()
            arg = int(arg)
            instructions += [{"op": op, "arg": arg}]
        return instructions

    def __build_test_case(self, instructions: List[Dict]):
        replacement = {"jmp": "nop", "nop": "jmp"}
        test_cases = []
        for idx, inst in enumerate(instructions):
            if inst["op"] in ["jmp", "nop"]:
                fixed_inst = copy.deepcopy(instructions)
                fixed_inst[idx]["op"] = replacement[inst["op"]]
                test_cases += [fixed_inst]
        return test_cases

    def __reset(self):
        self.__accumulator = 0
        self.__ran = []
        self.__p = 0
        self.__terminated = False

    def __boot(self, instructions):
        while self.__p not in self.__ran:
            if self.__p >= len(instructions):
                self.__terminated = True
                break
            inst = instructions[self.__p]
            op = inst["op"]
            arg = inst["arg"]
            self.__ran += [self.__p]
            if op == "acc":
                self.__accumulator += arg
                self.__p += 1
            elif op == "jmp":
                self.__p += arg
            elif op == "nop":
                self.__p += 1
        return self.__terminated
