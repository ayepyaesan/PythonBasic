base=int(input("Enter base: "))
power=int(input("Enter power: "))
onum=1

if power>0:
   while power!=0:
       onum*=base
       power-=1
   print("Result is ",onum)
else:
    while power!=0:
        onum*=base
        power+=1
    print("Result is ",1/onum)