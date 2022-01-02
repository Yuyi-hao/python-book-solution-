a,b,c = eval(input("Enter three edges : "))

sum = a+b+c
if (sum-max(a,b,c)) > max(a,b,c):
    print("The parameter is {}".format(sum))
else:
    print("The input is invalid")