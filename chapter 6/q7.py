# Financial  application:  calculate  future  investment  value
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):

    numberOfMonths = years*12 
    futureInvestmentvalue = investmentAmount*((1+monthlyInterestRate)**numberOfMonths)

    return futureInvestmentvalue

def main():
    investmentAmount = eval(input("Enter investment amount : "))
    annualInterestrate = eval(input("Enter annual interest rate in percent : "))
    years = eval(input("Enter number of years : "))
    monthlyInterestRate = annualInterestrate/1200
    print('Years \t \t Future Value')
    for i in range(1,years+1,1):
        futureValue = futureInvestmentValue(investmentAmount,monthlyInterestRate,i)
        print('{} \t \t {:.2f}'.format(i,futureValue))

main()

