a,b,c = eval(input('Enter the coefficients of first equation (ax+by=c) : '))
d,e,f = eval(input('Enter the coefficients of second equation (ax+by=c) : '))

i = a*d-b*c
if(i == 0):
    print("The equation has no solution")
else:
    x = (e*d-b*f)/i
    y = (a*f-e*c)/i
    print('x is {:.1f} and y is {:.1f}'.format(x,y))