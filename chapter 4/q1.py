# Algebra : solve quadratic equations 
a,b,c = eval(input("Enter the coefficients(ax^2+bx+c) : "))
d = b**2-4*a*c
if(d<0):
    print('The equation has no real roots')
elif(d==0):
    root = (-b)/(2*a)
    print('it has only one root which is {:.1f}'.format(root))
elif(d>0):
    root1 = (-b+d**0.5)/(2*a)
    root2 = (-b-d**0.5)/(2*a)
    print('It has two roots {:.1f} and {:.1f}'.format(root1,root2))
else:
    print('INVALID INPUT!!!')