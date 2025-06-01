# finance_calculator.py

# Prompt the user for financial details
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output the results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected annual savings after interest are: ${annual_savings:.2f}")
