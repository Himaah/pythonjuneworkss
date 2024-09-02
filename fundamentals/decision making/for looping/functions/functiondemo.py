# def cube(num):
#     result=num**3
#     return result

# print(cube(3))


# def max_two(n1,n2):
#     result=n1 if n1>n2 else n2
#     return result
# print(max_two(1,2))


# def is_odd(num):
#     result=True if num%2!=0 else False
#     return result
# print(is_odd(2))

# def leap_year(year):
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         return True
#     else:
#         return False
    
# print(leap_year(2035))

# create a fnctn with nth_digit_max with two parameter num1,num2
# nth_digit-max (123,480)

def nth_digit_max (num1,num2):
    digit1=num1%10
    digit2=num2%10

    if digit1>digit2:
        return num1 
    else:
        return num2
    
print(nth_digit_max(334,321))

# return num1 if num1%10>num2%10 else num2