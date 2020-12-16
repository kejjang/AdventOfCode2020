import json

from typing import List
from math import prod
from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        self.__parse_raw_data()
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        possible_values = self.__get_possible_values()
        error_rate = sum([sum([i for i in t if i not in possible_values]) for t in self.__nearby_tickets])
        return error_rate

    def __part2(self) -> int:
        self.__remove_invalid_tickets()
        keys = list(self.__fields.keys())
        field_keys = [json.loads(json.dumps(keys)) for _ in self.__your_ticket]
        field_possible_values = self.__get_field_possible_values()

        for t in self.__nearby_tickets:
            for i, v in enumerate(t):
                for k in field_possible_values:
                    if v not in field_possible_values[k]:
                        field_keys[i].remove(k)

        while len([k for k in field_keys if len(k) > 1]) > 0:
            for v in [k[0] for k in field_keys if len(k) == 1]:
                for i, k in enumerate(field_keys):
                    if v in k and len(k) > 1:
                        field_keys[i].remove(v)

        field_keys = [i[0] for i in field_keys]
        indexes = [i for i, v in enumerate(field_keys) if v[0:9] == "departure"]
        return prod([v for i, v in enumerate(self.__your_ticket) if i in indexes])

    def __parse_raw_data(self):
        self.__fields = {}
        self.__your_ticket = None
        self.__nearby_tickets = []

        pos1 = self.data.index("")
        raw_fields = self.data[:pos1]
        for f in raw_fields:
            key, ranges = f.split(":")
            key = key.strip().replace(" ", "_")
            ranges = [([int(i) for i in r.strip().split("-")]) for r in ranges.strip().split("or")]
            self.__fields[key] = ranges

        pos2 = self.data.index("your ticket:")
        self.__your_ticket = [int(i) for i in self.data[pos2 + 1].split(",")]

        pos3 = self.data.index("nearby tickets:")
        self.__nearby_tickets = [[int(i) for i in t.split(",")] for t in self.data[pos3 + 1 :]]

    def __get_field_possible_values(self):
        possible_values = {}
        for k in self.__fields:
            pv = []
            for r in self.__fields[k]:
                pv += list(range(r[0], r[1] + 1))
            possible_values[k] = list(set(pv))
        return possible_values

    def __get_possible_values(self) -> List[int]:
        possible_values = []
        field_possible_values = self.__get_field_possible_values()
        for k in field_possible_values:
            possible_values += field_possible_values[k]
        return list(set(possible_values))

    def __remove_invalid_tickets(self):
        possible_values = self.__get_possible_values()
        valid_ticktes = []
        for t in self.__nearby_tickets:
            valid = True
            for i in t:
                if i not in possible_values:
                    valid = False
            if valid:
                valid_ticktes += [t]
        self.__nearby_tickets = valid_ticktes
