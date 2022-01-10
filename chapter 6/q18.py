import random
def printMatrix(n):
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            num = random.randint(0,1)
            print(num,end=' ')
        print()

def main():
    n = int(input("Enter the order of square matrix : "))
    printMatrix(n)
main()