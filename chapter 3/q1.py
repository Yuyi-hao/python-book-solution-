import math as m 
r = eval(input("Enter the length from the center to a vertext : "))

side = 2*r*m.sin(m.pi/5)
area = 1.5*(3**0.5)*side**2

print('The area of pentagon is {:.2f}'.format(area))