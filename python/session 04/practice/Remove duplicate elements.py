list_char = []
chars = []
number = int(input("enter length of youre list: "))
for i in range(number):
    char = input("enter your char:\t")
    list_char.append(char)

for i in range(len(list_char)):
    if list_char[i] not in chars:
        chars.append(list_char[i])
print("your list:", list_char, "\nupdate list:", chars)