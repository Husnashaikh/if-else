age=int(input("enter the age:"))
if age>=18:
    print(age,"is eligible for voing")
elif age<18:
    print(age,"is not eligible for voting")
else:
    print("you are still a child")

num=int(input("enter the number:"))
a=num%10
if num%10:
    print("last digite is",a)
else:
    print("error")
