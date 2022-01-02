rate = eval(input("Enter the exchange rate from dollars to RMB : "))

convert = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa : "))

if convert == 0:
    amount = eval(input("Enter the dollar amount : "))
    print("${:.1f} is {:.1f} yuan".format(amount,(amount*rate)))
elif convert == 1:
    amount = eval(input("Enter the RMB amount : "))
    print("{:.1f} yuan is ${:.2f}  ".format(amount,(amount/rate)))
else:
    print("Incorrect input")