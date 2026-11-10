rows = 6
cols = 20

for x in range(rows):
    print(" " * (rows - x - 1), end="")

    for y in range(cols):
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

