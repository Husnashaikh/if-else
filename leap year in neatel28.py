leapyear=int(input("enter the number : "))
if leapyear%4==0:
    if leapyear%400==0:
        print("it is a century year")
    else:
        print("it is a leapyear")    
else:
    print("error")         