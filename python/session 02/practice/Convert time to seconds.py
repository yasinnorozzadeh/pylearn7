time = input("enter the time in this format:(01:20:45)\n")
time = time.split(":")
hour = int(time[0]) * 3600
minut = int(time[1]) * 60
print("seconds:", hour + minut + int(time[2]))

# or

# hours = int(input("enter hours: "))
# minuts = int(input("enter minuts: "))
# seconds = int(input("enter seconds: "))
# print("seconds:", (hours * 3600) + (minuts * 60) + seconds)