import math 
class Rectangle2D:
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def setX(self,x):
        self.__x = x
        return self.__x
    def setY(self,y):
        self.__y = y
        return self.__y
    def setWidth(self,width):
        self.__width = width
        return self.__width
    def setHeight(self,height):
        self.__height = height
        return self.__height

    def getArea(self):
        area = self.getWidth()*self.getHeight()
        return area
    def getPerimeter(self):
        perimeter = 2*(self.getHeight()+self.getWidth())
        return perimeter
    
    def containsPoint(self,x,y):
        dx = abs(self.__x-x)
        dy = abs(self.__y-y)
        if dx < self.__width/2 and dy < self.__height/2:
            return True
        else:
            return False
     
    def contains(self, rect):
        dis = math.sqrt((self.__x- rect.getX()) ** 2 + (self.__y - rect.getY()) ** 2)
        return True if dis + rect.getWidth() <= self.__width and dis + rect.getHeight() <= self.__height else False

    def overlaps(self, rect):
        xOvelLap = (self.getX() >= rect.getX() and self.getX() <= rect.getX() + rect.getWidth()) or \
                   (rect.getX() >= self.getX() and rect.getX() <= self.getX() + self.getWidth())
        yOverLap = (self.getY() >= rect.getY() and self.getY() <= rect.getY() + rect.getHeight()) or \
                   (rect.getY() >= self.getY() and rect.getY() <= self.getY() + self.getHeight())
        return xOvelLap and yOverLap

    def __contains__(self, rect):
        return True if rect.contains(self) else False

    def __lt__(self, rect):
        return self.__cmp__(rect) < 0

    def __le__(self, rect):
        return self.__cmp__(rect) <= 0

    def __eq__(self, rect):
        return self.__cmp__(rect) == 0

    def __ne__(self, rect):
        return self.__cmp__(rect) != 0

    def __gt__(self, rect):
        return self.__cmp__(rect) > 0

    def __ge__(self, rect):
        return self.__cmp__(rect) >= 0


def main():
    x1, y1, w1, h1 = eval(input("Enter centre x1, y1, width1, height1: "))
    x2, y2, w2, h2 = eval(input("Enter centre x2, y2, width2, height2: "))
    r1 = Rectangle2D(x1, y1, w1, h1)
    r2 = Rectangle2D(x2, y2, w2, h2)
    print("Area for r1 is", r1.getArea())
    print("Perimeter for r1", r1.getPerimeter())
    print("Area for r2 is", r2.getArea())
    print("Perimeter for r2", r2.getPerimeter())
    print("r1 contains the center of r2?", r1.containsPoint(r2.getX(), r2.getY()))
    print("r1 contains r2?", r1.contains(r2))
    print("r1 overlaps r2?", r1.overlaps(r2))


main()
