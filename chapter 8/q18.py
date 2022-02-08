import math
from operator import truediv 
class Circle2D:
    def __init__(self,x = 0.0,y=0.0,radius=0.0):
        self.__x = x
        self.__y = y
        self.__radius = radius
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getRadius(self):
        return self.__radius
    def setX(self,x):
        self.__x = x
        return self.__x
    def setY(self,y):
        self.__y = y
        return self.__y
    def setRadius(self,radius):
        self.__radius = radius
        return self.__radius
    def getArea(self):
        area = math.pi*self.__radius*self.__radius
        return area
    def getPerimeter(self):
        perimeter = 2*math.pi*self.__radius
        return perimeter
    def containsPoint(self,x,y):
        d = ((self.__x-x)**2+(self.__y-y)**2)**0.5
        if d<self.__radius:
            return True
        else:
            return False
     
    def contains(self,circle2D):
        d = ((self.__x-circle2D.getX())**2+(self.__y-circle2D.getY())**2)**0.5
        
    def overlaps(self,circle2D):
        d = math.sqrt((self.getX()-circle2D.getX())**2+(self.getY()-circle2D.getY())**2)
        if d<=(self.getRadius()+circle2D.getRadius()):
            return True
        else:
            return False

    def contains(self, circle2D):
        dis = math.sqrt((self.getX() - circle2D.getX()) ** 2 + (self.getY() - circle2D.getY()) ** 2)
        if self.getRadius() >= dis + circle2D.getRadius():
            return True
        else:
            return False
    def __lt__(self, circle2D):
        return self.__radius < circle2D.getRadius()

    def __gt__(self, circle2D):
        return self.__radius > circle2D.getRadius()

    def __ge__(self, circle2D):
        return self.getRadius() >= circle2D.getRadius()

    def __le__(self, circle2D):
        return self.getRadius() <= circle2D.getRadius()
    def __eq__(self, circle2D):
        return self.getRadius() == circle2D.getRadius()
    def __cmp__(self,circle2D):
        if self.__radius > circle2D.getRadius():
            return 1
        elif self.__radius < circle2D.getRadius():
            return -1
        else:
            return 0
    def __contains__(self,circle2D):
        if self.contains(circle2D):
            return True
        else:
            return False

def main():
    x1,y1,r1 = eval(input("Enter x y and radius of circle 1 : "))
    x2,y2,r2 = eval(input("Enter x y and radius of circle 2 : "))
    c1 = Circle2D(x1,y1,r1)
    c2 = Circle2D(x2,y2,r2)
    print(f'Area of c1 is {c1.getArea()}')
    print(f'Perimeter of c1 is {c1.getPerimeter()}')
    print(f'Area of c2 is {c2.getArea()}')
    print(f'Perimeter of c2 is {c2.getPerimeter()}')
    print(f'c1 contais the center of c2 ? {c1.containsPoint(x2,y2)}')  
    print(f'c1 contains c2 ? {c1.contains(c2)}')
    print(f'c1 overlaps c2? {c1.overlaps(c2)}')

main()