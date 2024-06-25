"""The formula for computing the final amount if one is earning compound interest"""

principal_amount = float(input("enter initial investiment: "))
annual_interest_rate = float(input("enter annual rate: "))
number_time_rate = int(input("enter number of time rate: "))
years = int(input("enter number of years: "))

#use () to break formula in two lines
final_amount: float = (principal_amount*(1 + annual_interest_rate/number_time_rate)
                       **(number_time_rate*years))

print(f"final amount is: {final_amount}")
#add empty newline to close the script
