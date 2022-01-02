import random

comp = random.randint(0,2)

if comp == 0:
    compChoice = 'Scissor'
elif comp == 1:
    compChoice = 'Rock'
elif comp == 2:
    compChoice = 'Paper'

print(compChoice)
user = int(input("Scissor (0), Rock (1), Paper (2) : "))

if user == 0:
    userChoice = 'Scissor'
elif user == 1:
    userChoice = 'Rock'
elif user == 2:
    userChoice = 'Paper'

if user == comp:
    print("The computer is {}, you are {} too. It is a draw".format(compChoice,userChoice))
elif user == comp+1 or (user ==0 and comp == 2) or (user == 2 and comp == 0):
    print("The computer is {}, you are {}. You won".format(compChoice,userChoice))
else:
    print("The computer is {}, you are {}. You lose".format(compChoice,userChoice))
    