sum = 0

tuloy = True

while tuloy ==True:
    x = int(input("PLEASE ENTER A NUMBER-->"))

    if x == 0:
        print("LOOP TERMINATED")
        break
    else:
        print("CONTINUE LOOP")
        sum += x
        print("CURRENT TOTAL IS ", sum)
        continue