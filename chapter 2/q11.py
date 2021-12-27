# Financial  application:  investment  amount

finalValue = eval(input("Enter final account value: "))
interestRate = eval(input("Enter annual interest rate in percent: "))
years = eval(input("Enter number of years: "))

numberOfMonths = years*12
monthlyInterestRate = interestRate/1200 
initialDepositAmount = finalValue/((1+monthlyInterestRate)**numberOfMonths)

print('Initial deposit value is {:.5f}'.format(initialDepositAmount))
