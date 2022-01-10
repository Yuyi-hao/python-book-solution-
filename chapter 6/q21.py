def sqrt(n):
    lastGuess = n
    init = 0.0001
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    while (lastGuess - nextGuess) >= init:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2

    return nextGuess


def main():
    number = int(input("Enter the number : "))
    print('The square root of {} is {:.4f}'.format(number,sqrt(number)))
main()