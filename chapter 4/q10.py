import random
a,b = random.randint(0,99),random.randint(0,99)

mul = a*b
userans = eval(input('Enter the sum of {}*{} = '.format(a,b)))

if(mul == userans):
    print("You did it right")
else:
    print("Wrong answer")
