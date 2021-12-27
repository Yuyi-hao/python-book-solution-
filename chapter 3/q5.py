import math 

n = int(input("Enter the number of sides : "))
side = eval(input("Enter the side of the pentagon : "))

area = (n*(side**2))/(4*math.tan(math.pi/n))
print("The area of the pentagon is {:.4f}".format(area))

