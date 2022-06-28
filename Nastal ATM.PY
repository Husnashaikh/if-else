print("WELCOME  TO ICIC BANK")
atm=input("enter the card")
if atm=="credit card" or atm=="debit card":
    print("next")
    language=input("enter the language")
    if  language=="hindi" or language=="english":
            print("next")
            account=input("select your account")
            if account=="saving account" or account== "current account":
                    print("continue with the saving account")
                    code=int(input("enter the code number 1 to 10"))
                    if code>=4:
                        print("wait for checking password")
                        amount=int(input("enetr the amount"))
                        if amount>500 or amount<=10000:
                            print("plz wait your tranzaction is in prosses")
                            recipt=input("want recipt")
                            if recipt=="yes" or recipt=="no":
                                print("transition successfully")
                                print("thank you")
                            else:
                                print("plz collect you recip")   
                        else:
                            print("the enter amount is not avilable") 
                    else:
                        print("plz check the enterd pin")
            else:
                print("plz check you account")
    else:
        print("check the language")
else:
    print("error")        