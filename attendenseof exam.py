classheld=int(input("enter the calssheld:"))
classattend=int(input("enter the classattend:"))
percentage=(classattend/classheld*100)
if percentage>=75:
    print("you are allow to sit for the exam:",int(percentage))
elif percentage<=75:
    print("you are not allow to sit for the exam:",int(percentage))
else:
    print("will not sit for the exam")



