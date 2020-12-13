import math

from functools import reduce
from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        self.__estimate_time = int(self.data[0])
        self.__bus_schedules = self.data[1].split(",")
        self.__bus_ids = list(map(int, filter(lambda item: item != "x", self.data[1].split(","))))
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)()

    def __part1(self) -> int:
        times = [i * math.ceil(self.__estimate_time / i) - self.__estimate_time for i in self.__bus_ids]
        return (min_time := min(times)) * self.__bus_ids[times.index(min_time)]

    # def __part2(self) -> int:  # crazy loops
    #     bus_rel_times = [self.__bus_schedules.index(str(i)) for i in self.__bus_ids]
    #     print(bus_rel_times)
    #     t = 100000000000000
    #     while 1:
    #         print(t)
    #         valid = True
    #         for i in range(1, len(bus_rel_times)):
    #             # print(f"{(t + bus_rel_times[i])} {self.__bus_ids[i]} {(t + bus_rel_times[i]) % self.__bus_ids[i]}")
    #             if (t + bus_rel_times[i]) % self.__bus_ids[i] != 0:
    #                 valid = False
    #                 break
    #         # break
    #         if valid:
    #             return t
    #         else:
    #             t += self.__bus_ids[0]

    def __part2(self) -> int:  # use chinese remainder theorem
        mods = {int(bus_id): (int(bus_id) - idx) % int(bus_id) for idx, bus_id in enumerate(self.__bus_schedules) if bus_id != "x"}
        mx = list(mods.keys())
        vx = list(mods.values())
        multiply = reduce(lambda acc, iter: acc * iter, mx, 1)
        Mx = [(multiply // item) for item in mx]
        tx = []
        for idx, val in enumerate(mx):
            t = 1
            while 1:
                if (t * Mx[idx]) % val == 1:
                    tx += [t]
                    break
                else:
                    t += 1
        result = sum([vx[i] * tx[i] * Mx[i] for i in range(len(mx))])
        while result - multiply > 0:
            result -= multiply
        return result
