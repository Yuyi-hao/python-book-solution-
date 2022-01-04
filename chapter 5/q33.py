amount = float(input("Enter the initial deposit amount : "))
annualInterestRate = float(input("Enter annual percentage yield(e.g. 5%) : "))
month = int(input("Enter maturity period (number of months) : "))

monthlyInterestRate = annualInterestRate/1200
monthlyAmount = amount
print("Month \t \t CD Value")
for i in range(1,month+1,1):
    monthlyAmount  = monthlyAmount+monthlyAmount*monthlyInterestRate
    print('{} \t \t {:.2f}'.format(i,monthlyAmount))

