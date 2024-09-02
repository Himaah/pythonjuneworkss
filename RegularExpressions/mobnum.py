# validate mobile number with country code mandatory
# ten digits only
# 6 7 8 9


from re import fullmatch

mobile_num="91 9446188907"

pattern="(91)\\s?[6-9][0-9]{9}"

matcher=fullmatch(pattern,mobile_num)

print("invalid" if matcher==None else "valid")