def isPrime(n):
    if n == 2:
        return True
    start = 2
    if n%2 == 0:
        return False
    else:
        while start<n:
            if n%start == 0:
                return False
            else:
                start+=1 
    return True
def reverse(n):
    reverse = ''
    for i in str(n):
        reverse = i+reverse
    return int(reverse)

def isPalindromic(n):
    reverse = ''
    for i in str(n):
        reverse = i+reverse
    if int(reverse) == n:
        return True
    return False

def format(number,width): 
    result = ''
    difference = width-len(str(number))
    if len(str(number)) > width or len(str(number)) == width:
        return int(str(number))
    else:
        while difference != 0:
            result += ' '
            difference -=1
    return result+str(number)

def main():
    n = 2
    count = 0
    while count < 100:
        if isPrime(n) and isPrime(reverse(n)) and not(isPalindromic(n)):
            count +=1
            fNumber = format(n,4)
            print(fNumber,end=' ')
            if count%10 ==0:
                print()
        n +=1

main()