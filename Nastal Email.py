print("Visit Google account creation page:")
email=input("want to creat email:")
if email=="yes":
    print("next")
    username=input("enter the name:")
    if username>"A" and username<"Z" or username>"a" and username<"z":
        print("next")
        lastname=input("enter the last name")
        if lastname>"A" and lastname<"z" or lastname>"a" and lastname<"z":
            print("next")
            number=int(input("enter the number"))
            if number<=1 or number>=1000000000:
                print("next") 
                birthday=int(input("enter the date of birth"))
                if birthday==birthday:
                    print("next")
                    gender=input("enter the gender")
                    if gender=="female":
                        print("next")
                        email=input("enter your own email adderes")
                        if email and "@gmail.com"in email:
                            print("next")
                            password=input("enter the password")
                            if password>="letters" and "other symbols" and"number":
                                print("your email is created")
                            else:
                             print("you password is wrong") 
                        else:
                            print("invailed adderes")   
                    else:
                        print("error")
                else:
                    print("cheak the date")
            else:
                print("re cheak")
        else:
            print("error")
    else:
        print("error")              
else:
    print("error")