month = int(input("Enter month (e.g. jan-1) : "))
year = int(input("Enter the year : "))

if month == 1:
    monthName = 'January'
    monthDays = 31
elif month == 2:
    monthName = 'February'
    if (year % 400 == 0) and (year % 100 == 0):
        monthDays = 29
    elif (year % 4 ==0) and (year % 100 != 0):
        monthDays = 29
    else:
        monthDays = 28
elif month == 3:
    monthName = 'March'
    monthDays = 31
elif month == 4:
    monthName = 'April'
    monthDays = 30
elif month == 5:
    monthName = 'May'
    monthDays = 31
elif month == 6:
    monthName = 'June'
    monthDays = 30
elif month == 7:
    monthName = 'July'
    monthDays = 31
elif month == 8:
    monthName = 'August'
    monthDays = 31
elif month ==  9:
    monthName = 'September'
    monthDays = 30
elif month == 10:
    monthName = 'October'
    monthDays = 31
elif month == 11:
    monthName = 'November'
    monthDays = 30
elif month == 12:
    monthName = 'December'
    monthDays = 31
else:
    print("INVALID INPUT 😡!!!")

print('{} {} has {} days. '.format(monthName,year,monthDays)) 
 
