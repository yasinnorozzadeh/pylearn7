list_char = []
list_char2 = []
number = int(input('enter number of your list: '))
for i in range (number):
    char = input("enter your character:\n")
    list_char.append(char)
for i in range(len(list_char), 0, -1):
    list_char2.append(list_char[i-1])
print("your list:", list_char, "\n", "opposite of your list:", list_char2)