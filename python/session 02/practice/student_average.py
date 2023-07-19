name = input("enter your name: ")
sum_scores = 0
counter = 0
while True:
    print("if you want to exit project enter | exit | command")
    score = input("enter youre score: ")
    if score.isalpha():
        score = None
        break

    sum_scores += float(score)
    print(float(score))
    counter += 1
average = sum_scores / counter
print(f"{name} your average is {average}")