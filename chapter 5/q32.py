amount = float(input("Enter the amount : "))
annualInterestRate = float(input("Enter annual interest rate (e.g. 5%) : "))
month = int(input("Enter duration in month : "))

monthlyInterestRate = annualInterestRate/1200
monthlyAmount = 0
for i in range(1,month+1,1):
    monthlyAmount  = (amount+monthlyAmount)*(1+monthlyInterestRate)

print('Your amount after {} months is {:.3f}'.format(month,monthlyAmount))