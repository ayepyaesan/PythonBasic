distance=float(input("Enter your destination distance in meter"))
time=float(input("Enter time to be reached in minutes"))

speed= distance / (time / 60 )
print("You have to ride", speed , 'mph')
