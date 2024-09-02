year=int(input("enter the year"))

if year%100==0:
    print(f"{year} is century year")
else:
    print(f"{year} is a non century year")