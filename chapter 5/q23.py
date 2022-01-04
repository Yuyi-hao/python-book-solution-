loanAmount = float(input("Enter the loan amount : "))
loanPeriod = int(input("Enter the loan period in year : "))
interestRate = 5
increment = 1/8
print('Interest Rate \t Monthly Payment \t Total Payment')
while (interestRate) <=8:
    monthlyInterestRate = interestRate/1200
    monthlyPayment = loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(loanPeriod*12))
    totalPayment = monthlyPayment*loanPeriod*12
    print('{:.3f}% \t \t {:.2f} \t \t {:.2f}'.format(interestRate,monthlyPayment,totalPayment))
    interestRate += increment