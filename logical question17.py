amount=int(input("enter the amount"))
note2000=note500=note200=note100=note50=note20=note10=note2=note1=0
if amount>=2000:
    print(amount//2000,"note2000")
elif amount>=500:
    print(amount//500,"note500")
elif amount>=200:
    print(amount//200,"note200")
elif amount>=100:
    print(amount//100,"note100")
elif amount>=50:
    print(amount//50,"note50")
elif amount>=20:
    print(amount//20,"note20")
elif amount>=10:
    print(amount//10,"note10")
elif amount>=2:
    print(amount//2,"note2")
elif amount>=1:
    print(amount//1,"note1")




