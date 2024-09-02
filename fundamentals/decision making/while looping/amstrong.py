num=int(input("enter the number"))

total=0
original=num
dig_count=len(str(num)) #to get the length in strings
while(num!=0):
    digit=num%10
    exponent=digit**dig_count
    total=total+exponent
    num=num//10

if(original==total):
    print(f"{original} is a an amstrong number")
else:
    print(f"{original} is not an amstrong number")
  
