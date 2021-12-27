# Sum the digits in an integer
# you can omit conditional statement it is just to check 

number = int(input("Enter a number between 0 to 1000 : "))

onePlace = number%10
number2 = number//10
tenth = number2%10
number3 = number2//10
sumOfDigit = onePlace+tenth+number3
if(number == 1000):
    print('The sum of the digits is 1')
elif(number<0 or number>1000):
    print("Enter number between 1 to 1000")
elif(number>0 or number<1000):
    print('The sum of the digits is {}'.format(sumOfDigit))
else:
    print('INVALID INPUT!!!')

