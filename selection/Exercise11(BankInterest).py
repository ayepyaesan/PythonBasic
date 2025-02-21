accountType=input("Enter your bank account type: Normal or Deluxe or Others: ")
loanPeriod=int(input("Enter your loan period: "))
loanAmount=int(input("Enter your loan amount: "))

if accountType=="Normal":
    if loanPeriod < 5:
        interest=loanAmount*0.15
    else:
        interest=loanAmount*0.17
elif accountType=="Deluxe":
    if loanPeriod < 10:
        interest=loanAmount*0.14
    elif loanPeriod>15:
        interest=loanAmount* 0.18
    else:
        interest=loanAmount* 0.16
else:
    interest=loanAmount*0.18

print("Your interest is ",int(interest))