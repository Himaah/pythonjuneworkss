text="ABCCDDBB"

word_count={}

for c in text:
    if c in word_count:
        print(c,"first recursive character")
        break
    else:
        word_count[c]=1

#which ever string object 'c'  comes into the else  part, it is stored in the dictionary as KEY.
# and VALUE is 1.
