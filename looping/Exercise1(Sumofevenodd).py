n=int(input("Enter a number: "))
evensum=0
oddsum=0
for i in range(1,n+1):
    if i%2==0:
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print("sum of all even number is: ",evensum)
print("sum of all odd number is: ",oddsum)
