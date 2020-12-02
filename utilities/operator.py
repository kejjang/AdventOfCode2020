from utilities.data import PuzzleInput


class Base:
    def __init__(self, day_num: int = -1):
        if day_num in range(1, 25):
            self.load_data(day_num)

    def load_data(self, day_num):
        self.data = PuzzleInput.get(day_num)
