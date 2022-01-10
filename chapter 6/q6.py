def displayPattern(n):
    for i in range(1,n+1,1):
        for j in range(n,i,-1):
            print(' ',end=' ')
        for k in range(i,0,-1):
            print(k,end=' ')
        print()

def main():
    num = int(input("Enter number of rows : "))
    displayPattern(num)
main()
