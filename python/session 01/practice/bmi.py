weight = float(input("enter your weight : "))
height = float(input("enter your height : "))
BMI = weight / (height ** 2) 
print("youre bmi  is:", BMI)
if BMI > 35:
    result = "extremely obese"
elif 30 < BMI < 34.9:
    result = "obese"
elif 25 < BMI < 29.9:
    result = "over wight"
elif 18.5 < BMI < 24.9:
    result = "normal"
else:
    result = "under weight"
print(result)