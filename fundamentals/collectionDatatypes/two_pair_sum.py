arr=[2,3,4,5]

result=6
total=0
for i in range (0,len(arr)):
    total=total+arr[i]
    if total>=result:
        print(arr[i])
