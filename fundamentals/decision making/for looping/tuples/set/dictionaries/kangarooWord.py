source_word="REGULATE"
target_word="RULE"

word_count={}

for w in source_word: #w=hello

    if w in word_count:             #if w is in word count then increment

        word_count[w]+=1

    else:

        word_count[w]=1

is_Kangaroo=True       #SETTING A VARIABLE 


for w in target_word:

    if w in word_count and word_count.get(w)>0:    #get is used to get the value of w

        word_count[w]-=1


    else:
        is_Kangaroo=False

        break


print(is_Kangaroo)






# word_countt={}
# for i in source_word:
#     if i in word_countt:
#         word_countt[i]+=1
#     else:
#         word_countt[i]=1

# is_Kangarooo=True

# for i in target_word:
#     if i in word_countt and word_countt.get(i)>0:
#         word_countt[i]-=1
#     else:
#         is_Kangarooo=False

# print(is_Kangarooo)
