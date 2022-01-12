import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y 
    # accessor and mutator
    def getN(self):
        return self.__n
    def getSide(self):
        return self.__side
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setN(self,N):
        self.__n = N
        return self.__n
    def setSide(self,newSide):
        self.__side = newSide
        return self.__side
    def setX(self,x):
        self.__x = x
        return self.__x
    def setY(self,y):
        self.__y = y
        return self.__y
    
    def getPerimeter(self):
        return self.__n*self.__side
    def getArea(self):
        area = (self.__n*self.__side*self.__side)/(4*math.tan(math.pi/self.__n))
        return area

def main():
    rp1 = RegularPolygon()
    rp2 = RegularPolygon(6,4)
    rp3 = RegularPolygon(10,4,5.6,7.8)
    print("Regular polygon 1")
    print('Number of sides : {}\nLength of side : {}\ncenter : ({},{})\nArea : {:.4f}\nPerimeter : {}'.format(rp1.getN(),rp1.getSide(),rp1.getX(),rp1.getY(),rp1.getArea(),rp1.getPerimeter()))
    print()
    print("Regular polygon 2")
    print('Number of sides : {}\nLength of side : {}\ncenter : ({},{})\nArea : {:.4f}\nPerimeter : {}'.format(rp2.getN(),rp2.getSide(),rp2.getX(),rp2.getY(),rp2.getArea(),rp2.getPerimeter()))
    print()
    print("Regular polygon 3")
    print('Number of sides : {}\nLength of side : {}\ncenter : ({},{})\nArea : {:.4f}\nPerimeter : {}'.format(rp3.getN(),rp3.getSide(),rp3.getX(),rp3.getY(),rp3.getArea(),rp3.getPerimeter()))

main()
