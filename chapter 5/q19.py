n = int(input("Enter a integer between (1-15) : "))
k = 0
if n>=1 and n<=15:
    for i in range(1,n+1,1):
        for j in range(n,i,-1):
            print(end = '  ')
        while k != i:
            for l in range(i,0,-1):
                print(l, end = ' ')
            k +=1
        for m in range(2,i+1,1):
            print(m, end = ' ')
        print()
else:
    print("You've entered a digit which is greater than 15 or lesser than 1 ") 