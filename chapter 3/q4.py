import math 

side = eval(input("Enter the side of the pentagon : "))
area = (5*(side**2))/(4*math.tan(math.pi/5))
print("The area of the pentagon is {:.4f}".format(area))

