from listing11 import getRandomCharacter
def main():
    A = 1
    for i in range(10000):
        char = getRandomCharacter('A','Z')
        if char == 'A':
            A +=1
    print('Probability of A is : {:.4f}'.format(A/10000))

main()