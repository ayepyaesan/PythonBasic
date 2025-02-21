remainingHours=int(input("Enter remaining hour "))
remainingMinutes=int(input("Enter remaining minutes"))
remainingSeconds=int(input("Enter remaining seconds"))

totalSeconds=remainingHours*60*60 + remainingMinutes*60 + remainingSeconds
print('Total Seconds',totalSeconds)