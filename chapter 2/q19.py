# Financial  application:  calculate  future  investment  value

investmentAmount = eval(input("Enter investment amount : "))
annualInterestrate = eval(input("Enter annual interest rate in percent : "))
years = eval(input("Enter number of years : "))

numberOfMonths = years*12
monthlyInterestRate = annualInterestrate/1200 

futureInvestmentvalue = investmentAmount*((1+monthlyInterestRate)**numberOfMonths)

print("Accumulated value is {:.3f}".format(futureInvestmentvalue))