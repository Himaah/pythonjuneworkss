# validate pancard
#  first 3 alphabets
# PCAFHT 4th place
# 1 alphabet in 5th place
# 4 digit
# 1 alphabet

from re import fullmatch
pancard_no="AFZPK7190K"
pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,pancard_no)
print("invalid" if matcher==None else "valid")



