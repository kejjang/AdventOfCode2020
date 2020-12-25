from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        self.data = [int(i) for i in self.data]
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, pub_keys) -> int:
        loop_size = []
        start_value = 1
        for key in pub_keys:
            value = start_value
            subject_number = 7
            t = 0
            while 1:
                value = value * subject_number % 20201227
                t += 1
                if value == key:
                    break
            loop_size += [t]

        value = start_value
        subject_number = pub_keys[0]
        for _ in range(loop_size[1]):
            value = value * subject_number % 20201227

        return value

    def __part2(self, pub_keys) -> int:
        return "Merry Christmas"
