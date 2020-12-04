import re

from itertools import chain
from utilities.operator import Base


class Operator(Base):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def exec(self, rule: int = 1):
        rules = {1: self.__rule1, 2: self.__rule2}
        if rule not in rules:
            return 0

        passports = (" ".join(self.data)).split("  ")
        counter = 0

        for passport in passports:
            fields = dict(zip(items := iter(list(chain.from_iterable([items.split(":") for items in passport.split()]))), items))
            counter += 1 if rules.get(rule, lambda x: False)(fields) else 0

        return counter

    def __rule1(self, fields):
        keys = self.keys.copy()
        keys.remove("cid")
        return False if len(set(keys) - set([item[0] for item in fields.items()])) > 0 else True

    def __rule2(self, fields):
        sub_rules = {"byr": self.__sub_rule_byr, "iyr": self.__sub_rule_iyr, "eyr": self.__sub_rule_eyr, "hgt": self.__sub_rule_hgt, "hcl": self.__sub_rule_hcl, "ecl": self.__sub_rule_ecl, "pid": self.__sub_rule_pid}
        return self.__rule1(fields) and (1 > sum([sub_rules.get(key, lambda x: 0)(fields[key]) for key in fields]))

    def __sub_rule_byr(self, value: str):
        return 0 if value.isdigit() and int(value) in range(1920, 2003) else 1

    def __sub_rule_iyr(self, value: str):
        return 0 if value.isdigit() and int(value) in range(2010, 2021) else 1

    def __sub_rule_eyr(self, value: str):
        return 0 if value.isdigit() and int(value) in range(2020, 2031) else 1

    def __sub_rule_hgt(self, value: str):
        return 0 if (unit := value[-2:]) in ["cm", "in"] and (quantity := value[0:-2]).isdigit() and (((unit == "cm") and (int(quantity) in range(150, 194))) or ((unit == "in") and (int(quantity) in range(59, 77)))) else 1

    def __sub_rule_hcl(self, value: str):
        return 0 if 1 == len(re.findall(r"#[0-9a-f]{6}", value)) else 1

    def __sub_rule_ecl(self, value: str):
        return 0 if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else 1

    def __sub_rule_pid(self, value: str):
        return 0 if value.isdigit() and len(value) == 9 else 1
