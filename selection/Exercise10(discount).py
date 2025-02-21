item=input("Enter your item: clothe or shoe: ")
price=int(input("Enter your price: "))
if item=="clothe":
    if price<20:
        profit=price*0.1
    elif price<50 or price>20:
        profit=price*0.15
    else:
        profit=price*0.2
else:
    if price<5 or price>30:
        profit=price*0.05
    else:
        profit=price*0.1

print("Your profit is ",profit)