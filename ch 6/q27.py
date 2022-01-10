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

def main():
    for i in range(1,1001,1):
        if isPrime(i) and isPrime(i+2):
            print(f'({i}, {i+2})')
main()