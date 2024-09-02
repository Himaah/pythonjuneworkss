
# fullmatch()is used to return the exact match. 
# fullmatch() returns the exact match not iterable so for looping is not used. 
# It returns None if no match is present.

from re import fullmatch

variable_name=input("enter the variable name")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)

print("invalid" if matcher==None else "valid")


