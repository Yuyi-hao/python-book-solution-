today = int(input("Enter today's day : "))
dayElapsed = int(input("Enter the number of days elapsed since today : "))
print

if(today == 0):
    day = 'Sunday'
elif(today == 1):
    day = 'Monday'
elif(today == 2):
    day = 'Tuesday'
elif(today == 3):
    day = 'Wednesday'
elif(today == 4):
    day = 'Thuresday'
elif(today == 5):
    day = 'Friday'
elif(today == 6):
    day = 'Saturday'

if((dayElapsed+today)%7 == 0):
    nextday = 'Sunday'
elif((today+dayElapsed)%7 == 1):
    nextday = 'Monday'
elif((today+dayElapsed)%7 == 2):
    nextday = 'Tuesday'
elif((today+dayElapsed)%7 == 3):
    nextday = 'Wednesday'
elif((today+dayElapsed)%7 == 4):
    nextday = 'Thuresday'
elif((today+dayElapsed)%7 == 5):
    nextday = 'Friday'
elif((today+dayElapsed)%7 == 6):
    nextday = 'Saturday'

print('Today is {} and the future day is {} '.format(day,nextday))







