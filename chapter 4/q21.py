
year = int(input("Enter year : "))
month =  int(input("Enter month 1-12 :"))
date = int(input("Enter the day of the month 1-31: "))
dayOfWeek = ''

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
        dayOfWeek = 'Sunday'
    elif h>0 and h<=1:
        dayOfWeek = 'Monday'
    elif h>1 and h<=2:
        dayOfWeek = 'Tuesday'
    elif h>2 and h<=3:
        dayOfWeek = 'Wednesday'
    elif h>3 and h <= 4:
        dayOfWeek = 'Thursday'
    elif h> 4 and h <= 5.5:
        dayOfWeek = 'Friday'
    elif h >5.5:
        dayOfWeek = 'Saturday' 

    print("Day of the week is {}".format(dayOfWeek))
