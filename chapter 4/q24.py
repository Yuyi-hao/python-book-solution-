import random 

num,card = random.randint(1,13),random.randint(1,4)

if num == 1:
    number = 'Ace'
elif num == 2:
    number = '2'
elif num == 3:
    number = '3'
elif num == 4:
    number = '4'
elif num == 5:
    number = '5'
elif num == 6:
    number = '6'
elif num == 7:
    number = '7'
elif num == 8:
    number = '8'
elif num == 9:
    number = '9'
elif num == 10:
    number = '10'
elif num == 11:
    number = 'Jack'
elif num == 12:
    number = 'Queen'
elif num == 13:
    number = 'King'

if card == 1:
    suit = 'Clubs'
elif card == 2:
    suit = 'Diamonds'
elif card == 3:
    suit = 'Hearts'
elif card == 4:
    suit = 'Spades'

print("The card you picked is the {} of {}".format(number,suit))








