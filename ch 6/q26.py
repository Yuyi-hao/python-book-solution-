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
    print('p \t 2^p-1')
    i = 1
    p = 0
    while p <= 31:
        if isPrime(i):
            while (2**p)-1 <= i:
                if (2**p)-1 == i:
                    print(f'{p} \t {i}')
                    break
                else:
                    p +=1
        i +=1

main()