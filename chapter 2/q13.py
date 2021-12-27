# you can omit conditional statement it is just to check 

number = int(input("Enter a four digit number: "))

onePlace = number%10
number2 = number//10
tenth = number2%10
number3 = number2//10
hundredth = number3%10
number4 = number3//10

print("digits\n{}\n{}\n{}\n{}\n".format(number4,hundredth,tenth,onePlace))