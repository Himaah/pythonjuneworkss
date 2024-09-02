# extract numbers from a digit

num=int(input("enter the number"))

while(num!=0): #loop has to work till num=0

    digit=num%10
    num=num//10
    print(digit)
    
    