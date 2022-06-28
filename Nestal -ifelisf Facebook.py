print("Visit Google account creation page:")
facebook=input("want to creat facebook account")
if facebook=="yes":
    print("next")
    username=input("enter the name:")
    if username>"A" and username<"Z" or username>"a" and username<"z":
        print("next")
        lastname=input("enter the last name")
        if lastname>"A" and lastname<"z" or lastname>"a" and lastname<"z":
            print("next")
            number=int(input("enter the number"))
            if number>=8 or number>=1000000000:
                print("next") 
                birthday=int(input("enter the date of birth"))
                if birthday==birthday:
                    print("next")
                    gender=input("enter the gender")
                    if gender=="female":
                        print("next")
                        print("your account is made")
                    else:
                        print("error")
                else:
                    print("re-check") 
            else:
                print("invalid number")   
        else:
            print("error")
    else:
        print("change the username") 
else:
    print("stop")