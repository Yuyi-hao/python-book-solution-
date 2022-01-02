import random 

comp = random.randint(0,1)
if comp == 0:
    compCoin = 'heads'
else:
    compCoin = 'tails'

guess = eval(input(" For head type 1 and for tails 2 : "))

if guess == comp:
    print("You're correct {}".format(compCoin))
else:
    print("You're wrong {}".format(compCoin))