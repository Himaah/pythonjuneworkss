text="ABABCDE"

# PRINT ALL NON RECURSIVE CHARACTERS
# WORD_COUNT={A:2  B:2  C:1  D:1  E:1}


word_count={}
for c in text:
    if c in word_count:
        word_count[c]+=1
    else:
        word_count[c]=1

for k,v in word_count.items():      #to select as key:value pair .items is used
    if v==1:             #when the value of v is 1 it is not repeated
        print (k)          #k is printed       
            