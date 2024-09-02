# str built_ins.py
# string defines method capitalize
# method calling - object.method
# if word is string object : word.capitalize
# object creation - object name = class
# thunder.start

# word="the quick brown fox jump over the lazy dogs"
# alphabet="abcdefghijklmnopqrstuvwxyz"
# word=word.casefold()
# is_pangram=True

# for ch in alphabet:
#     if word.count(ch)==0:
#         is_pangram= False
#         break
# print(is_pangram)
# text="pneumonoultramicroscopicsilicovolcanoconiosis"
# vowels="aeiou"
# text=text.casefold()
# v_count=0
# for ch in text:    #text ilnne nokkaavu.
#     if vowels.count(ch)==0:    
#         v_count+=1 
# print(v_count)

text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="aeiou"
text=text.casefold()
v_count=0
c_count=0
for ch in text:    #text ilnne nokkaavu.
    if vowels.count(ch)!=0:    
        v_count+=1 
    else:
        c_count+=1
print(v_count)
print(c_count)



text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels="aeiou"
text=text.casefold()
v_count=0
for ch in text:    #text ilnne nokkaavu.
    if vowels.count(ch)==0:    
        v_count+=1 
print(v_count)




# print(word.capitalize())

# print(word.upper())

# print(word.lower())

# print(word.index("z"))

# print(word.isalpha())

# print(word.isdigit())

# print(word.isalnum()) #alphabet or num

# print alphabets in the sentence

# for characters in word:
#     if characters.isalpha():
#         print(characters,end= ',')

# for dig in word:
#     if dig.isdigit():
#         print(dig,end=' ')

# print(word.count("l"))

# print(word.count("y"))

# 




