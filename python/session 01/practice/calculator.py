import math
print("welcome to my calculator!")
op = input("+ : sum\n- : sub\n* : mul\n/ : div\n1 : sin\n2 : cos\n3 : tan\n4 : cot\n5 : sqrt\n6 : factorial\n7 : log\nenter your choice:\t")
if op == "+" or op == "-" or op == "*" or op == "/":
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
else:
    number = float(input("enter number: "))
if op == "+" or op == "sum":
    result = num1 + num2
elif op == "-" or op == "sub":
    result = num1 - num2
elif op == "*" or op == "mul":
    result = num1 * num2
elif op == "/" or op == "div":
    if num2 == 0:
        result = "cannot divide by zero"
    else:
        result = num1 / num2
elif op == "sin" or op == "1":
    result = math.sin(math.radians(number))
elif op == "cos" or op == "2":
    result = math.cos(math.radians(number))
elif op == "tan" or op == "3":
    result = math.tan(math.radians(number))
elif op == "cot" or op == "4":
    result =  math.cos(math.radians(number) / math.sin(math.radians(number)))
elif op == "sqrt" or op == "4":
    result = math.sqrt(number)
elif op == "factorial" or op == "5":
    result = math.factorial(number)
elif op == "log" or op == "6":
    result = math.log(number)
else:
    result = "cannot find youre operation"
print(result)