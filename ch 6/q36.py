from listing11 import getRandomCharacter

def main():
    count = 0
    for i in range(100):
        print(getRandomCharacter('A','Z'),end=' ')
        count +=1
        if count%10 == 0:
            print()
    count = 0
    print()
    for i in range(100):
        print(getRandomCharacter('0','9'),end=' ')
        count +=1
        if count%10 == 0:
            print()

main()