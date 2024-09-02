# numbers=(1,2,3,4)    #tuple defined by()

# print(numbers[1])    #index positioning,duplicates allow, immutable index(),count()

numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]

new_num=list(num)

new_num.append(500)

print(tuple(new_num))

numbers[2][1]=tuple(new_num)

print(numbers)



# duplicates allow,index position ,insertion order same,not mutable, if one elt is there give ,

# count(),index() - methods