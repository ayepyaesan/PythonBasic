amount=int(input("Enter your amount: "))
type=input("Enter your customer type: regular or premium ")
if type=="regular":
    if amount > 500:
        amount -= amount*0.1
        print("10% discount and your final price is ",amount)
    else:
        amount -= amount*0.05
        print("5% discount and your final price is ",amount)
else:
    if amount > 500:
        amount -= amount*0.2
        print("20% discount and your final price is ",amount)
    else:
        amount -= amount*0.15
        print("15% discount and your final price is ",amount)
