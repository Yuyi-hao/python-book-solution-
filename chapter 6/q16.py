def numberOfDaysInYear(year):
    if year%4 == 0 and year%100 != 0:
        return 366
    else:
        return 365


def main():
    print('Years \t \t Numbers of days')
    for i in range(2010,2021,1):
        print('{} \t \t {}'.format(i,numberOfDaysInYear(i)))
main()
