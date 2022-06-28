a=int(input("enyter the side:"))
b=int(input("enter the side:"))
c=int(input("enter the side:"))
if a==b==c:
    print("equliteral triangle")
elif a==b or b==c or c==a:
    print("isoceilies triangle")
elif a!=b!=c:
    print("scalen triangle")
else:
    print("invalid triangle")