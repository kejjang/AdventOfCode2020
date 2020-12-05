from utilities.operator import Base


class Operator(Base):
    def exec(self, part: int = 1):
        return (parts := {1: self.__part1, 2: self.__part2}).get(part if part in parts else 1)(self.data)

    def __part1(self, b_pass_all):
        return max(self.__get_all_seat_id(b_pass_all))

    def __part2(self, b_pass_all):
        seats = ["0"] * 8 * 128
        for i in self.__get_all_seat_id(b_pass_all):
            seats[i] = "1"
        return "".join(seats).index("101") + 1

    def __get_all_seat_id(self, b_pass_all):
        return [self.__get_seat_id(b_pass) for b_pass in b_pass_all]

    def __get_seat_id(self, b_pass):
        rows, cols = b_pass[:7], b_pass[7:]
        row_range = [0, 127]
        col_range = [0, 7]

        row = [self.__shrink_range(row_range, type) for type in rows][0][0]
        col = [self.__shrink_range(col_range, type) for type in cols][0][0]

        return row * 8 + col

    def __shrink_range(self, pos_range, type):
        if type in ["F", "L"]:
            pos_range[1] = pos_range[0] + (pos_range[1] - pos_range[0]) // 2
        elif type in ["B", "R"]:
            pos_range[0] = (sum(pos_range) + 1) // 2
        return pos_range
