row = int(input("enter row: "))
col = int(input("enter col: "))
for i in range(col):
    if i % 2 == 0:
        for j in range(1, row+1):
            if j % 2 == 0:
                print("⬜", end=(""), sep="")
            else:
                print("⬛", end=(""), sep="")
    else:
        for j in range(row):
            if j % 2 == 0:
                print("⬜", end=(""), sep="")
            else:
                print("⬛", end=(""), sep="")
    print()