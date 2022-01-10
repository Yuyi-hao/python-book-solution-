
def getPentagonalnumber(n):
    return n*(3*n - 1)/2

def main():
    n=int(input("Enter how many pentagonal numbers you want :  "))
    for i in range(1,n+1):
        print(int(getPentagonalnumber(i)),"\t", end='')
        if  i%10==0:
            print()

main()