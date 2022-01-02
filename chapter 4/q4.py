import random
a,b = random.randint(0,100),random.randint(0,100)

sum = a+b
userSum = eval(input('Enter the sum of {}+{} = '.format(a,b)))

if(sum == userSum):
    print("You did it right")
else:
    print("Wrong answer")