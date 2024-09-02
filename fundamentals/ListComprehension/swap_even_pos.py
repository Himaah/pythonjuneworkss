arr=[10,11,12,13,14,15,16,17]
#     0  1  2  3  4  5  6  7
# odd pos num= [11 13 15 17]
#  rev odd pos=[17 15 13 11]
# [10 17 15 14 13 16 11]
# odd_position = [arr[num] for num in range(1, len(arr), 2)]
# print(odd_position)


left=1
length=len(arr)-1
print(length)
right= length if length%2!=0 else length-1

while (left<right):
    (arr[left],arr[right])=(arr[right],arr[left])       #swapping
    left=left+2
    right=right-2
print(arr)



# words=["fly","float","flower","flat"]

# find common prefix fl
#  extract smallest word
# smallest_word = min(words, key=len)
# for ch in words:
#     if ch.startswith(smallest_word):
#         print (ch)
#     else:
#        smallest_word=smallest_word[:-1]
#     print (smallest_word)


# words = ["fly", "float", "flower", "flat"]

# prefix = min(words, key=len)

# for word in words:
#     while not word.startswith(prefix):
#         prefix = prefix[:-1]

#     if not prefix:
#         print("not common prefix")
#         break

# print(f"Common Prefix: {prefix}")


