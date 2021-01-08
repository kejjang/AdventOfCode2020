from os import path

for day_num in range(1, 26):
    filename = f"day{day_num:02d}.py"
    if path.exists(filename):
        print(f"running {filename}\n")
        exec(open(filename).read())
        print("\n================================\n")
