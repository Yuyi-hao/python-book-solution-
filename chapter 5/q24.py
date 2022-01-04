loanAmount = float(input("Enter the loan amount : "))
loanPeriod = int(input("Enter the loan period in year : "))
interestRate = float(input("Enter the annual interest rate : "))
k = 1

monthlyInterestRate = interestRate/1200
monthlyPayment = loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(loanPeriod*12))
totalPayment = monthlyPayment*loanPeriod*12

print(totalPayment-(monthlyPayment*1))
print('Monthly Payment : {:.2f}'.format(monthlyPayment))
print('Total Payment : {:.2f}'.format(totalPayment))
print('Payment Month \t Interest \t Principal \t \t Balance')
balance = loanAmount
while k<=12:
    interest = monthlyInterestRate*balance 
    principal = monthlyPayment - interest
    balance = balance- principal 
    print('{:.2f} \t \t {:.2f} \t \t {:.2f} \t \t {:.2f}'.format(k,interest,principal,balance))
    k+=1
