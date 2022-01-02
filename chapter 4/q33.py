num = eval(input("Enter a decimal value (0 to 15) : "))
if num < 15 and num>-1: 
    if num ==0:
        hex = 0
    elif num ==1:
        hex = 1
    elif num ==2:
        hex =2
    elif num ==3:
        hex =3
    elif num ==4:
        hex =4
    elif num ==5:
        hex =5
    elif num ==6:
        hex =6
    elif num ==7:
        hex =7
    elif num ==8:
        hex =8
    elif num ==9:
        hex =9
    elif num ==10:
        hex ='A'
    elif num ==11:
        hex ='B'
    elif num ==12:
        hex ='C'
    elif num ==13:
        hex ='D'
    elif num ==14:
        hex ='E'
    elif num ==15:
        hex ='F'
    print("The hex value is {}".format(hex))
else:
    print("Invalid input")
