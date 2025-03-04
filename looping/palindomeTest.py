num=int(input("Enter number: "))
reversenum=0

while num!=0:
    reversenum=reversenum*10+num%10
    num=num//10
print("Reverse number:",reversenum)