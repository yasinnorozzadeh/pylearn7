number = int(input("the number of elements of the Fibonacci sequence: "))
numbers_list = [1, 1]
if 0 <= number  <= 2:
    if number == 0:
        print(" ")
    elif number == 1:
        print("1 ")
    else:
        print("1 1")

elif number > 2:
    for i in range(1, number-1):
        numbers_list.append(numbers_list[i - 1 ]+ numbers_list[i])

print(numbers_list)