import re

from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, part: int = 1):
        self.__parse_raw_data()
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        rule = self.__get_regex_of_rule_0()
        # print(rule)
        count = 0
        for m in self.__messages:
            if len(re.findall(r"^" + rule + r"$", m)) > 0:
                count += 1
        return count

    def __part2(self) -> int:
        """
        new rules:
        8: 42 | 42 8
        11: 42 31 | 42 11 31
        """
        self.__change_rules({"8": " ( 42 )+ ", "11": " ( 42 ){n} ( 31 ){n} "})
        rule = self.__get_regex_of_rule_0()
        # print(rule)
        count = 0
        for m in self.__messages:
            for i in range(1, (max([len(i) for i in self.__messages]) + 1) // 2):
                xrule = rule.replace("{n}", f"{{{i}}}")
                if len(re.findall(r"^" + xrule + r"$", m)) > 0:
                    count += 1
                    break
        return count

    def __parse_raw_data(self):
        pos = self.data.index("")
        self.__rules = self.__parse_rules(self.data[0:pos])
        self.__messages = self.data[pos + 1 :]

    def __parse_rules(self, rules_raw):
        rules = {}
        for line in rules_raw:
            key, data = [i.strip() for i in line.split(":")]
            rules[key] = " " + data.replace('"', "") + " "
        return rules

    def __get_regex_of_rule_0(self):
        rule = self.__rules["0"]
        while len(re.findall(r"\d+", rule)) > 0:
            keys = re.findall(r"\d+", rule)
            for key in keys:
                rule = re.sub(r"\s" + key + r"\s", f" ({self.__rules[key]}) ", rule)
        rule = rule.replace(" ", "")
        while len(re.findall(r"\(([ab]+)\)", rule)) > 0:
            rule = re.sub(r"\(([ab]+)\)", r"\1", rule)
        return rule

    def __change_rules(self, new_rules):
        for k in new_rules:
            self.__rules[k] = new_rules[k]
