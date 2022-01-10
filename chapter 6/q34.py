import math 

def area(side,n):
    
    area = (n*(side**2))/(4*math.tan(math.pi/n))
    return area

def main():
    n = int(input("Enter the number of sides : "))
    side = eval(input("Enter the side of the pentagon : "))

    Area = area(side,n)
    print("The area of the pentagon is {:.4f}".format(Area))
main()