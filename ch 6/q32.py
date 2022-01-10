def format(number,width): 
    result = ''
    difference = width-len(str(number))
    if len(str(number)) > width or len(str(number)) == width:
        return int(str(number))
    else:
        while difference != 0:
            result += ' '
            difference -=1
    return result+str(number)
count = 0

def getMonthBody(year,month):
    count = 0
    for j in range(getStartDay(year,month)):
        print(end='     ')
        count +=1
    for i in range(1,getTotalNumberOfDaysInMonth(year,month)+1,1):
        i = format(i,3)
        print(i,end='  ')
        count +=1
        if count%7 == 0:
            print()

def getMonthName(month):
    monthName = ''
    if month == 1:
        monthName =  'January'
    elif month == 2:
        monthName =  'February'
    elif month == 3:
        monthName =  'March'
    elif month == 4:
        monthName =  'April'
    elif month == 5:
        monthName =  'May'
    elif month == 6:
        monthName =  'June'
    elif month == 7:
        monthName =  'July'
    elif month == 8:
        monthName =  'August'
    elif month == 9:
        monthName =  'September'
    elif month == 10:
        monthName =  'October'
    elif month == 11:
        monthName = 'November'
    else:
        monthName = 'December'
    return monthName

def getStartDay(year,month):
    date = 1
    if month == 2 and date > 29:
        print("Invalid date february only has 28 or 29 days")
    else:
        if month == 1 or month == 2:
            month = month+12
            year = year-1
        q = date
        m = month
        j = year//100+1
        k = year%100
        h= ((q+(26*(m+1)/10)+k+(k/4)+(j/4)+5*j)%7)
        if h == 0:
           h = 0
        elif h>0 and h<=1:
           h = 1
        elif h>1 and h<=2:
           h = 2
        elif h>2 and h<=3:
           h = 3
        elif h>3 and h <= 4:
           h = 4
        elif h> 4 and h <= 5.5:
           h = 5
        elif h >5.5:
           h = 6 
        return h 

def isLeap(year):
    if year%400 or (year%4==0 and year%100 !=0):
        return True
    else:
        return False

def getTotalNumberOfDaysInMonth(year,month):
    if (month == 1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        return 31
    elif (month==4 or month==6 or month==9 or month  ==11):
        return 30
    if month == 2:
        return 29 if isLeap(year) else 28
    print('total number of days')

def printMonthTitle(year,month):
    print(f'\t{getMonthName(month)} \t {year}')
    print('----------------------------------')
    print('Sun  Mon  Tue  Wed  Thu  Fri  Sat')

def printMonth(year,month):
    printMonthTitle(year,month)
    getMonthBody(year,month)

def main():
    year = int(input("Enter year : "))
    for i in range(1,13,1):
        printMonth(year,i)
        print('\n\n')

main()