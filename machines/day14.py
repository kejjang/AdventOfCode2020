import re

from itertools import product
from collections import defaultdict
from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        mask = None
        memory = defaultdict(dict)
        for line in self.data:
            if line[0:4] == "mask":
                mask = line.split("=")[1].strip()
            elif line[0:4] == "mem[":
                items = re.findall(r"^mem\[(\d+)\]\s=\s(\d+)$", line.strip())
                v = [int(item) for item in items[0]]
                nv = int("".join(map(lambda item: item[0] if item[1] == "X" else item[1], zip(("0" * 36 + bin(v[1])[2:])[-36:], mask))), 2)
                memory[v[0]] = nv
        return sum(memory.values())

    def __part2(self) -> int:
        mask = None
        memory = defaultdict(dict)
        for line in self.data:
            if line[0:4] == "mask":
                mask = line.split("=")[1].strip()
            elif line[0:4] == "mem[":
                items = re.findall(r"^mem\[(\d+)\]\s=\s(\d+)$", line.strip())
                v = [int(item) for item in items[0]]
                new_addr_with_mask = "".join(list(map(lambda item: item[0] if item[1] == "0" else item[1], zip(("0" * 36 + bin(v[0])[2:])[-36:], mask))))
                mask_pos = [i for i, m in enumerate(new_addr_with_mask) if m == "X"]
                n = len(mask_pos)
                products = product(["0", "1"], repeat=n)
                for p in products:
                    new_addr = list(new_addr_with_mask)
                    for j in range(n):
                        new_addr[mask_pos[j]] = p[j]
                    new_addr = "".join(new_addr)
                    memory[int(new_addr, 2)] = v[1]
        return sum(memory.values())
