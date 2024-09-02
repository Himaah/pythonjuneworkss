# bmi calculation
# bmi= (wght in kg/ht in m.sq)


weight_in_kg= 72
height_in_cm=165
#converting height into meter sq
height_in_msq= 165/10000
print(height_in_msq)

bmi_value= weight_in_kg//height_in_msq
print (f"bmi_value= {weight_in_kg}//{height_in_msq}={bmi_value}")



