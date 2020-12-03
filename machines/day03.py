from utilities.operator import Base


class Operator(Base):
    def exec(self, slope=False):
        if slope is False:
            return False

        pos = [0, 0]
        counter = 0

        while pos[1] < len(self.data):
            counter += 1 if self.data[pos[1]][pos[0] % len(self.data[0])] == "#" else 0
            pos = list(map(sum, zip(pos, slope)))

        return counter
