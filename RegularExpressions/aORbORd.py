#IMP :
#  [] to find seperate patterns give it in square brackets
# ==========================================================================

# [abf]" either a or b or f
# [ starting - ending] to find some starting to ending and its case sensitive
# [a-z] check all the lowercase alphabets
# [A-Z] check alll the upercase alphabets
# [a-zA-Z] print all alphabets
# [0-9]  check the digits
# [A-Za-z0-9] check for all alphanumeric character
# [^] EXCLUDE the specified 
# [\s] check for space
# [^a-zA-Z0-9\s] to print all the special characters
# [a-z]{3} to print 3 consecutive pattern of alphabets
# ([c-h]|[t-z]) to print all alphabets in text from c-h and t-z
# {} Quantifiers
# \d : print digits
# \D : exclude digits
# \w : print uppercase,lowercase and numbers
# \W : exclude uppercase lowercasr alphabets and numbers(spl cahr and space)
# \S : exclude space
# \s : space
# + : match one or more
# ? :  optional
# * :  zero or more

# ===========================================================================


from re import finditer

text="ab12xyz67 8#$pqr123cdefADS"


# pattern="[abf]" either a or b or f

# pattern="[a-k]"

# pattern="[a-z]"

# pattern="[A-Z]"

# pattern="[A-Za-z]"

# pattern="[^a-zA-Z0-9\s]"

# pattern="[a-z0-9]{3}"

# pattern="[c-ht-z]"

# pattern="([a-z]{3}|[A-Z]{3}|[0-9]{3})"

pattern="\S"

matching_pattern=finditer(pattern,text)

for m in matching_pattern:
    print(m.start(), "====", m.group())



