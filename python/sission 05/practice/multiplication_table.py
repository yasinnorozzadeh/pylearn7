from termcolor import colored

row = int(input("enter row: "))
col = int(input("enter col: "))
print(colored("x", "yellow"), sep="", end="\t")
for i in range(1, col+1):
    print(colored(i, "yellow"), end="\t")
print()
for i in range(1, row+1):
    print(colored(i, "yellow"), end="\t", sep="")
    for j in range(1, col+1):
        if i == j:
            print(colored((j * i), "yellow"), end = "\t")
        else:
            print(j * i, end = "\t")

    print()
