# loan amount int RATE TENURE RATE
loan_amount= 100000
intrest_rate= 9/12/100
num_of_years=2 
num_of_months=24

print(intrest_rate)
emi=loan_amount*intrest_rate*(1+intrest_rate)**num_of_months/((1+intrest_rate)**num_of_months -1)
print(emi)
total_payable_amount= emi*num_of_months
print(f"total payable amount={total_payable_amount}")


# total_interestt= loan_amount*intrest_rate*num_of_years
total_interest= total_payable_amount-loan_amount
print(f"total interest payable ={total_interest}")




# print(f"emi=loan_amount*intrest_rate*(1+intrest_rate)**num_of_months/((1+intrest_rate)**num_of_months -1)= {emi}")
# print(f"emi= {emi}")