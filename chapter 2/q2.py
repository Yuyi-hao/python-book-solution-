# Compute the volume of a cylinder

#importing math module optional you can use a pi constant for it 

import math
length,radius = eval(input("Enter the length and radius of a cylinder (length,radius) : "))
area =radius*radius*math.pi
volume = area*length

print('The Area of base is {:.2f} \nThe volume is {:.2f}'.format(area,volume))
