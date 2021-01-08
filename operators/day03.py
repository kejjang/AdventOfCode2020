from utilities.operator import OperatorBase


class Operator(OperatorBase):
    def exec(self, slope=False):
        if slope is False:
            return False

        pos = [0, 0]
        counter = 0

        while pos[1] < len(self.data):
            counter += 1 if self.data[pos[1]][pos[0] % len(self.data[0])] == "#" else 0
            pos = [p + s for p, s in zip(pos, slope)]

        return counter
