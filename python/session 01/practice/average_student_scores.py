score1 = float(input("enter first score: "))
score2 = float(input("enter second score: "))
score3 = float(input("enter third score: "))
average = (score1 + score2 + score3)  / 3

if average >= 17:
    result = "great"
if average < 12:
    result = "fail"
else:
    result = "normal"
print(f"you are {result}")