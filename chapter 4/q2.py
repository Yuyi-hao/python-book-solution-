import random
a,b,c = random.randint(0,9),random.randint(0,9),random.randint(0,9)

sum = a+b+c
userSum = eval(input('Enter the sum of {}+{}+{} = '.format(a,b,c)))

if(sum == userSum):
    print("You did it right")
else:
    print("Wrong answer")