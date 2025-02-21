roomLength=float(input("Enter room length"))
roomWidth=float(input("Enter room width"))
roomHeight=float(input("Enter room height"))
paintPrice=float(input("Enter price of a gallon of paint"))
squareFeetGallonPaint=float(input("Enter square feet that a gallon of paint will cover"))

roomTotalArea= 2 * roomLength * roomHeight + 2 * roomWidth * roomHeight

print("Room Total Area is" ,roomTotalArea)

totalGallon= roomTotalArea / squareFeetGallonPaint
roundUpGallon= int(totalGallon + 0.9999)

print("Total Number of Gallons is",totalGallon)
print("Round Up Gallon is",roundUpGallon)

totalCost= roundUpGallon * paintPrice
print("Total cost for a room is", totalCost)
