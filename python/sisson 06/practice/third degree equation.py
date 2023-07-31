import math
def equation(a, b, c):
    p = b - ((a**2)/3)
    q = (2*(a**3)/27) - ((a*b)/3) + c
    delta = ((q**2)/4) + ((p**3)/27)
    if delta > 0:
        print("delta > 0")
        x = ((-1*(q/2) + math.sqrt(delta))**(1/3)) + ((-1*(q/2) - math.sqrt(delta))**(1/3)) - (a/3)
        return x
    elif delta == 0:
        print("delta == 0")
        x1 = -2((q/2)**(1/3)) - (a/3)
        x2 = ((q/2)**(1/3)) - (a/3)
        text = str(x1), "and", str(x2)
        return text
    elif delta < 0:
        x1 = (2/math.sqrt(3))*(math.sqrt(-1*p))*math.sin((1/3)*math.sin(((3*q*math.sqrt(3))/(2*(math.sqrt(-1*p) ** 3)))**-1))-(a/3)
        x2 =  (-2/math.sqrt(3))*(math.sqrt(-1*p))*math.sin((1/3)*math.sin(((3*q*math.sqrt(3))/(2*(math.sqrt(-1*p) ** 3)))**-1) + (math.pi/3))-(a/3)
        x3 =  (2/math.sqrt(3))*(math.sqrt(-1*p))*math.cos((1/3)*math.sin(((3*q*math.sqrt(3))/(2*(math.sqrt(-1*p) ** 3)))**-1) + (math.pi/6))-(a/3)
        text = str(x1), "and", str(x2), "and", str(x3)
        return text
a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
print(equation(a, b, c))