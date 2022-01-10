def series(m):
    sum = 0
    for i in range(1,m+1,1):
        sum += ((-1)**(i+1))/(2*i - 1)
    return 4*sum 

def main():
    print('i \t \t m(i)')
    print()
    for i in range(1,1000,100):
        print('{} \t \t {:.4f}'.format(i,series(i)))
main()