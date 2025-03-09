############################################################################

monthly_income = float(input('Enter your monthly income: '))
monthly_expenses = float(input('Enter your total monthly expenses: '))

# Calculate monthly income and monthly savings
monthly_savings = monthly_income - monthly_expenses

#Assume a simple annual interest rate of 5% and add to monthly savings 
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f'Projected savings after one year, with interest, is: {projected_savings}')

############################################################################
