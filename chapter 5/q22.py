count = 0
NUMBERS_PER_LINE = 8 
target = NUMBERS_PER_LINE
for i in range(2,1001,1):
    isPrime = True
    divisor = 2

    while divisor <= i/2:
        if i % divisor == 0:
            isPrime = False
            break 
        divisor +=1
    if isPrime:
        count +=1
        print(i,end=' ')
        if count == target:
            print()
            target += NUMBERS_PER_LINE


