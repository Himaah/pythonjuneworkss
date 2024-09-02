num=int(input("enter the number"))
previous=0
current=1
isFibo=False
org=current
next=previous+current

while(next<=num):
    next=previous+current
    previous=current
    current=next

    if(next==num): #check if fib
        isFibo=True

        break

print(isFibo)