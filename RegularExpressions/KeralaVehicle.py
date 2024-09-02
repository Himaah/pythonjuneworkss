# kerala vehicle number

# first 2 dig KL
# 2 digits
# alphabets (one or two)
# digits (4)

from re import fullmatch

reg_number="KL-08-BN-4970"

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"     #(KL) : Exact K and L ; {1,2} : min 1 max 2
# ? : at most 1
# pattern="(KL)\d{2}[A-Z]{1,2}\d{4}"


matcher=fullmatch(pattern,reg_number)

print("invalid" if matcher==None else "valid")