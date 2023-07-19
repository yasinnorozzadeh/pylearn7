import random
print("welcome to guess number game")
while True:
    counter = 1
    # number = random.randint(0, 100)
    number = 50
    while True:
        user_number = int(input("enter your number(range 0 to 100):\n"))
        if user_number == number:
            print("you win")
            break
        elif user_number > number:
            print("go down")
        else:
            print("go up")
        counter +=1
    print("your number of guesses: ", counter)
    try_again = input("do you want to try again?(y, n): ")
    if try_again != "y":
        break
print("good bye!")