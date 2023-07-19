import random

random_numbers_list = []
c = 0   #counter
number = int(input("enter your number for repeat the numbers: "))
while True:
    number_random = random.randint(0, 20)
    if not(number_random in random_numbers_list):
        random_numbers_list.append(number_random)
        c += 1
    if c == number:
        break
print(random_numbers_list)