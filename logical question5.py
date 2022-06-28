# Write a program to find the largest number out of two numbers excepted from user.

num=int(input("enter the number"))
num1=int(input("enter the number"))
if num<=num1 and num1>=num:
    print(num1,"largest number")
else:
    print(num,"greates number")