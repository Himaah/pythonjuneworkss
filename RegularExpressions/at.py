# findall  to find the list of specified
# returns the list of the specified
# just print the matcher
# any combination can be denoted with period.


from re import findall

text="the fat cat run away very fast to catch rat"

pattern=".at"

matcher=findall(pattern,text)

print(matcher)
