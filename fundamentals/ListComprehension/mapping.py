arr=[6,7,3,4,8,9,10]

# map if num>5 then num+1 and num<5 then num-1


mapped_lst= [num+1 if num>5 else num-1 for num in arr ]
print(mapped_lst)