def isPrime(n):
    i = 2
    while i<= n/2:
        if n%i == 0:
            return False
        i +=1
    return True
def main():
    print('Number \t \t Prime')
    n = 1
    count = 0
    NUMBER_PER_LINE = 15
    target = NUMBER_PER_LINE

    while n < 10001:
        if isPrime(n):
            print(n,end='  ')
            count +=1
        if count == target:
            print()
            target +=NUMBER_PER_LINE
        n +=1
main()