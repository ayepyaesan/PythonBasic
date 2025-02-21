n=int(input("Enter a number "))
if n%2==0:
    if n>=0:
        print(n," is Even Positive")
    else:
        print(n," is Even Negative")
else:
    if n>=0:
        print(n," is Odd Positive")
    else:
        print(n," is Odd Negative")