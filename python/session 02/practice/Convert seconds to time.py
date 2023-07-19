seconds = int(input("enter seconds: "))
hours = seconds // 3600
minuts = (seconds % 3600) // 60
seconds -= (hours * 3600) + (minuts * 60)

print(f"{hours}:{minuts}:{seconds}")