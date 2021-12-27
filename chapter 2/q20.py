# Financial application: calculate interest

balance,interestrate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

monthlyInterest = balance*(interestrate/1200)
print('The interest is {:.5f}'.format(monthlyInterest))