# 1st char uppercase alphabet
# next character digit 1-9 
# next digit 0-9
# 4th place 0 or one white space
# next 4 characters any number from 0 to 9
# last charcter 1-9

from re import fullmatch
passport="S71 19937"
pattern="[A-Z][1-9]\\d(0\\s)\\d{4}[1-9]"

matcher=fullmatch(pattern,passport)
print("invalid" if matcher==None else "valid")
