import math

from operators.day03 import Operator

op = Operator(day_num=3)

print("# Part One")
print(op.exec(slope=[3, 1]))

print("")

print("# Part Two")
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(math.prod([op.exec(slope=slope) for slope in slopes]))
