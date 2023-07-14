import math
print("welcome to my calculator!")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sin")
print("log")
print("enter your choice")
op = input()
if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
else:
    a = float(input("enter number: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "cannot divide by zero"
    else:
        result = a / b
elif op == "sin":
    result = math.sin(a)
elif op == "log":
    result = math.log(a)

print(result)