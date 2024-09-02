lst=[10,2,4,5]

#variable= [return iteration condition]

squares=[n**2 for n in lst ]

cubes=[n**3 for n in lst ]

print(squares)

print(cubes)


# print even and odd

even=[n for n in lst if n%2==0]
odd=[n for n in lst if n%2!=0]

print (odd)
print (even)