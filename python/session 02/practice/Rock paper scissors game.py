import random
list_game_characters = ["rock", "paper", "scissors"]
try_if = False
while True:
    computer_choice = random.choice(list_game_characters)
    user_choice = int(input("0_rock\t1_paper\t2_scissors\nenter your choice number: "))
    if 0 <= user_choice <= 2:
        if computer_choice == list_game_characters[user_choice] :
            print("equal")
            try_if = True
        elif (computer_choice == "rock" and list_game_characters[user_choice] == "scissors") or (computer_choice == "scissors" and list_game_characters[user_choice] == "paper") or (computer_choice == "paper" and list_game_characters[user_choice] == "rock"):
            print("computer win")
            try_if = True
        elif (list_game_characters[user_choice] == "rock" and computer_choice == "scissors") or (list_game_characters[user_choice] == "scissors" and computer_choice == "paper") or (list_game_characters[user_choice] == "paper" and computer_choice == "rock") :
            print("user win")
            try_if = True
        print("computer :", computer_choice, "\tuser :", list_game_characters[user_choice])
    else:
        print("your number is not in range(0 to 2)")
    if try_if:
        try_again = input("do you want to try again?(y, n): ")
        if try_again != "y":
            break
