currentyear=int(input("enter the current year"))
birthyear=int(input("date of birth"))
if currentyear-birthyear:
    print(currentyear-birthyear)
elif currentyear>birthyear:
    print(currentyear>birthyear)
else:
    print("error")