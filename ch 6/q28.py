import random
# rolling dice
def rollingDice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1,d2

def main():
    d1,d2 = rollingDice()
    print(f'Your rolled {d1}+{d2}={d1+d2}')
    if d1+d2 == 2 or d1+d2==3 or d1+d2==12:
        print('You loose')
    elif d1+d2 == 7 or d1+d2 == 11:
        print('You win')
    else:
        point = d1+d2   
        print(f'Point is {point}') 
        while True:
            d3,d4 = rollingDice()

            print(f'Your rolled {d3}+{d4}={d3+d4}')
            if d3+d4 == 7:
                print('You loose')
                break
            elif d3+d4 == point:
                print('You win')
                break 
main() 