side1 = int(input("enter side1:\t"))
side2 = int(input("enter side2:\t"))
side3 = int(input("enetr side3:\t"))

if (side1 + side2 - side3) > 0 and (side1 + side3 - side2) > 0 and (side2 + side3 - side1) > 0:
    result = "can"
else:
    result = "can not"

print(f"A triangle {result} be formed")
