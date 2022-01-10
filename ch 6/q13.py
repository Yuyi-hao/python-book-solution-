def series(m):
    sum = 0
    for i in range(1,m+1,1):
        sum += i/(i+1)
    return sum 

def main():
    print('i \t \t m(i)')
    print()
    for i in range(1,21,1):
        print('{} \t \t {:.4f}'.format(i,series(i)))
main()