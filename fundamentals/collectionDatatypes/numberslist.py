numbers=[10,11,12,34,43,54,19,78,42]

# no of objects
# even numbers
# total 
# total of odd

# 1

print(len(numbers))

#2

for i in range (0,len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])


# 3

total=0
for i in range(0,len(numbers)):
    total+=numbers[i]
print(total)


# 4


odd_total=0
for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        odd_total+=numbers[i]
print(odd_total)