numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]
new=numbers[2]

new_num=list(num)

new.pop()

new.insert(1,4)

num=numbers[2]

list_num=num
list_num=num[2][1]
list_num=list(num)
list_num.insert(1,150)

list_num=new_num
print(tuple(new_num))


print(numbers)