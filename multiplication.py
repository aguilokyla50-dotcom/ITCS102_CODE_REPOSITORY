col = int(input(" NU8MBER OF COLUMNS--> "))

for x in range (1, 11):
    for y in range (1, col, 1):
        print(x, "x",y,"=",x*y, end="\t")
    print()