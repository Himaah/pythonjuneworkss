arr=[
    [10,20],
    [21,30],
    [40,53]
]

evens=[num for lst in arr for num in lst if num%2==0]
print(evens)

numbers=[num for lst in arr for num in lst]
print(sum(numbers))

gt_fif=[num for lst in arr for num in lst if num>15]
print(gt_fif)