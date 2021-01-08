import re

from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, rule: int = 1):
        rules = {1: self.__rule1, 2: self.__rule2}
        if rule not in rules:
            return 0
        valid = 0
        for item in self.data:
            params = re.findall(r"(\d+)\-(\d+)\s(.):\s(.*)", item)[0]
            valid += 1 if rules.get(rule)(params) else 0
        return valid

    def __rule1(self, params):
        return True if params[3].count(params[2]) in range(int(params[0]), int(params[1]) + 1) else False

    def __rule2(self, params):
        return True if (a := params[3][int(params[0]) - 1]) != (b := params[3][int(params[1]) - 1]) and params[2] in [a, b] else False
