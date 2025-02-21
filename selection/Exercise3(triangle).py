a=float(input("Enter first length of triangle"))
b=float(input("Enter second length of triangle"))
c=float(input('Enter third length of triangle'))
if a+b <c or a+c <b or b+c<a:
    print("Not a valid triangle")
else:
    if a==b==c:
        print("Equilateral: All sides are equal")
    elif a==b or b==c or a==c:
        print("Isosceles: Exactly two sides are equal")
    else:
        print("Scalene: All sides are different")