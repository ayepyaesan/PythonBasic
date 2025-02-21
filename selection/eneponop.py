n=int(input("Enter a number "))
if n%2==0 and n>=0:
    print(n,"is Even Positive")
elif n%2==0 and n<0:
    print(n,"is Even Negative")
elif n%2!=0 and n>=0:
    print(n, "is Odd Positive")
else:
    print(n,"is Odd Negative")