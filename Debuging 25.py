num=int(input("enter the number::"))
if num%5==0 and num%15==0:
    print("divisible by both")
elif num%5==0:
    print("divisible by 5")
elif num%15==0:
    print("divisible by 15")
else:
    print("error")