import random
while True:
    random_dice = random.randint(1, 6)
    print("dice number: ", random_dice)
    while random_dice == 6:
        random_dice = random.randint(1, 6)
        print("chance again :", random_dice)
    try_again = input("do you want to try again?(y, n)")
    if not(try_again == "y"):
        break