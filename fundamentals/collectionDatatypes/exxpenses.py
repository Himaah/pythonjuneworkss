expenses=[12000,13000,11000,14000,15000,21000,22000,13000]

# count of objects
# all expenses
# expenses>15000
# total expense

# 1

expense_count=len(expenses)
print(expense_count)


# 2

for i in range(0,expense_count):
    print(expenses[i])


# 3

for i in range(0,len(expenses)):

    if expenses[i]>15000:

        print(expenses[i])

# total expense

total=0
for i in range(0,len(expenses)):
    total=total+expenses[i]
print(total)


# 4

total=0
avg=0
for i in range(0,len(expenses)):
    total=total+expenses[i]
    avg=total//len(expenses)
print(avg)




