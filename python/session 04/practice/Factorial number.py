number = int(input("enter your number: "))
number_fact = 1
def faktorial(number, number_f):
    check = False
    for i in range(2 , number+1):
        number_f *= i
        if number_f == number:
            check = True
            return "your number is factorial"
    if number <= 0 or check == False:
        return "youre number is not factorial"  
print(faktorial(number, number_fact))