import random
# rolling dice
def rollingDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1,d2

def game():
    d1,d2 = rollingDice()
    if d1+d2 == 2 or d1+d2==3 or d1+d2==12:
        return 'loose'
    elif d1+d2 == 7 or d1+d2 == 11:
        return 'You win'
    else:
        point = d1+d2   
        while True:
            d3,d4 = rollingDice()
            if d3+d4 == 7:
                return 'loose'
            elif d3+d4 == point:
                return 'You win'

def main():
    n = 10000
    winningCount = 0
    for i in range(n):
        roll = game()
        if roll == 'You win':
            winningCount +=1
    print('Your winning probability is {:.5f}'.format(winningCount/n))
main()