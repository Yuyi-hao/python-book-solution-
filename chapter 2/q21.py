# Financial application: compound value using for loop 

monthlySavingAmount = eval(input("Enter the monthly saving amount: "))
# months = eval(input("Enter no. of months : "))
MONTHLY_INTEREST_RATE = 0.00417

total = 0

# for i in range(0,months,1):
#     total = (monthlySavingAmount+total) * (1 + MONTHLY_INTEREST_RATE)

total = (monthlySavingAmount+total) * (1 + MONTHLY_INTEREST_RATE)
total = (monthlySavingAmount + total) * (1 + MONTHLY_INTEREST_RATE)
total = (monthlySavingAmount + total) * (1 + MONTHLY_INTEREST_RATE)
total = (monthlySavingAmount + total) * (1 + MONTHLY_INTEREST_RATE)
total = (monthlySavingAmount + total) * (1 + MONTHLY_INTEREST_RATE)
total = (monthlySavingAmount + total) * (1 + MONTHLY_INTEREST_RATE)
print("After the sixth month, the account value is",total)

