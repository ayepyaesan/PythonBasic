for i in range(50):
    print(i,end=" ")
print("\n")
for j in range(100,-1,-5):
    print(j,end=" ")

print(" ")

total=0
startPoint=int(input("Enter your start point: "))
endPoint=int(input("Enter your end point: "))
for i in range(startPoint,endPoint+1):
    print(i,end=",")
    total=total+i
print("\nTotal= ",total)
avg=total/(endPoint-startPoint+1)
print("\nAverage= ",avg)


