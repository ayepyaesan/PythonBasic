day=input("What day is Today? ")
age=int(input("Enter your age"))
if age<12:
    if day== 0 or day== 6:
        print("Movie Ticket price is $8")
    else:
        print("Movie Ticket price is $5")
elif age<=59:
    if day == 0 or day == 6:
        print("Movie Ticket price is $12")
    else:
        print("Movie Ticket price is $10")
else:
    if day==0 or day==6:
        print("Movie Ticket price is $7")
    else:
        print("Movie Ticket price is $5")