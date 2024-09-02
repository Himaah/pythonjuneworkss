# validate month

from re import fullmatch

valid_date=input("enter date")

pattern="(0?[1-9]|1[0-9]|2[0-9|3[0-1])"

matcher=fullmatch(pattern,valid_date)

if matcher==None:

    print("invalid")

else:
    
    print("valid")