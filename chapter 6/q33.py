import math 

def area(side):
    area = (5*(side**2))/(4*math.tan(math.pi/5))
    return area

def main():
    side = eval(input("Enter the side of the pentagon : "))
    Area = area(side)
    print("The area of the pentagon is {:.4f}".format(Area))
main()