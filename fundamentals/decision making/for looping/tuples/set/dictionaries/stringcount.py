text="hello hai hello hai hello"

# split the string

words=text.split(" ")    #split using what 
word_count={}      #creating an empty dict


for w in words: #w=hello

    if w in word_count:             #if w is in word count then increment
        word_count[w]+=1

    else:
        word_count[w]=1
print(word_count)