num = input("Enter a hex value (0 to F) : ").lower()

decimal = ''
if num == '0':
    decimal = 0
elif num == '1':
    decimal = 1
elif num == '2':
    decimal =2
elif num == '3':
    decimal =3
elif num =='4':
    decimal =4
elif num =='5':
    decimal =5
elif num =='6':
    decimal =6
elif num == '7':
    decimal =7
elif num == '8':
    decimal =8
elif num == '9':
    decimal =9
elif num == 'a':
    decimal ='10'
elif num == 'b':
    decimal =11
elif num == 'c':
    decimal =12
elif num == 'd':
    decimal= 13
elif num == 'e':
    decimal=14
elif num == 'f':
    decimal= 15
if decimal == '':
    print("Invalid input")
else:
    print('The decimal value of {} is {}'.format(num,decimal))
