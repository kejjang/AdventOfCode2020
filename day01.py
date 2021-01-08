from operators.day01 import Operator

op = Operator(day_num=1, to_int=True)

print("# Part One")
print(op.exec(entries=2))

print("")

print("# Part Two")
print(op.exec(entries=3))
