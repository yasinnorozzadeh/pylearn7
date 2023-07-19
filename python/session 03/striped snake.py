length_snake = int(input("enter length of snake:\n"))

for i in range(length_snake):
    if i // 2 * 2 == i:
        print("*", end="", sep="")
    else: 
        print("#", end="")
    
print()
