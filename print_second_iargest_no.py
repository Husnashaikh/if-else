a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a<b<c or c<b<a:
    print(b)
elif b<a<c or c<a<b:
    print(a)
elif a<c<b or b<c<a:
    print(c)
else:
    print("equal")