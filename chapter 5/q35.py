for i in range(1,10000,1):
# i = 28
    n = 1
    sum = 0
    while n < i:
        if i%n == 0:
            sum +=n
        n +=1
    if sum == i:
        print(i)