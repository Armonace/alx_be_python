monthly_income = int(input("enter your monthly income:"))
monthly_expenses = int(input("enter your monthly expenses:"))
x = monthly_income
y = monthly_expenses
#simplify the informations to simple terms to better carryout a clean work
monthly_savings = x - y
# using an assumed rate of 5%
project_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Projected savings after one year, with interest, is ", project_annual_savings)