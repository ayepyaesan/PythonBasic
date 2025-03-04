n=int(input("Enter some random number: "))
ans=0
while n!=0:
    ans+=n%10
    n=n//10
print("Sum of digits= ",ans)