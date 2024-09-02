num=int(input("enter the number"))
cube=0

while(num!=0):
    digit=num%10
    exponent=digit**3
    cube=exponent+cube
    num=num//10

print(cube)