# to split a text "split" can be used.

emil_id="johnsmith @gmail.com"
username,emil=emil_id.split(" ")

print(username)
print(emil)


# # starts with specific character - startswith
text="hello world"
print(text.startswith("he"))


# # ends with specific character - endswith
text="hello world"
print(text.endswith("l"))

# # to remove - strip(" ")
# # rstrip(" ")
# # lstrip(" ")

text1="/nhello/nworld/n"
print(text1.rstrip("/n"))
print(text1.lstrip("/n"))
print(text1.strip("/n"))

print(text1.replace("/n"," "))

# slicing

# sting_obj[start:end]
# sting_obj[start:]
# sting_obj[:end]

word="hellopython"

sliced= word[0:5]
print(sliced)

sliced2=word[5:11]
print(sliced2)

sliced3=word[5:]
print(sliced3)

sliced4=word[:11]
print(sliced4)

reverse=word[::-1]
print(reverse)


