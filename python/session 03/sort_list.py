len_number= int(input("enter length of youre numbers: "))
numbers_list = []
for i in range(len_number):
    number = float(input("enter your number: "))
    numbers_list.append(number)
error = 0
for i in range(1, len(numbers_list)):
    if numbers_list[i-1] <= numbers_list[i]:
        error += 0

    else:
        error += 1
print(numbers_list)
if error != 0:
    print("your numbers is not sort")
else:
    print("your numbers is sort")