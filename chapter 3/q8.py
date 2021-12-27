# Financial application : monetary units 

# Receive the amount
amount = int(input("Enter an amount, for example, 1156: "))
cents = amount%100
dollars = amount // 100
print('Your amount is {} cents and {} dollars'.format(cents,dollars))