class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def distance(self, point):
        d = ((self.__x-point.getX())**2+(self.__y-point.getY())**2)**0.5
        return d
    def isNear(self,point):
        d = self.distance(point)
        if d<5:
            return True
        else:
            return False
    def __str__(self):
        return '( ' + str(self.__x) + ',' + str(self.__y) + ' )'

def main():
    x1,y1 = eval(input("Enter points 1 (x,y) : "))
    x2,y2 = eval(input("Enter points 2 (x,y) : "))
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    print("The distance between the two points is {:.3f}".format(p1.distance(p2)))
    print("Is points are near to each other? : {}".format(p1.isNear(p2)))
main()
