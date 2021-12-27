# Geometry : great circle distance 

import math 
x1,y1 = eval(input("Enter point 1 (latitude and longitude) : "))
x2,y2 = eval(input("Enter point 2 (latitude and longitude) : "))

RADIUS= 6371.01
# calculation of great circle distance 

d = RADIUS * math.acos(math.sin(math.radians(x1))* math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2)))

print('The distance between the two points is {:.5f}'.format(d))