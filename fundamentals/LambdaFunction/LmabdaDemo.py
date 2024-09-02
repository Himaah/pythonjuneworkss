# add=lambda n1,n2: n1+n2
# print(add(10,20))


# sub=lambda n1,n2:n1-n2
# print(sub(10,5))

# cube=lambda n:n**3
# print(cube(3))

# max=lambda n1,n2:n1 if n1>n2 else n2
# print(max(100,200))

last_dig_max=lambda n1,n2: n1 if n1%10>n2%10 else n2
print(last_dig_max(127,872))


odd_even= lambda n1: "even" if n1%2==0 else "odd"
print(odd_even(10))




# min=lambda n1,n2:n1 if n1<n2 else n2
# print(min(100,200))