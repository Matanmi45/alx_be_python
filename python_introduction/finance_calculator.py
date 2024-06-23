monthlyIncome = input("Enter your montly income:\n")
monthlyExpenses = input("Enter your total monthly expenses:\n")

monthlySavings = int(monthlyIncome) - int(monthlyExpenses)

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print(f"Your monthly savings are ${monthlySavings}")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}")