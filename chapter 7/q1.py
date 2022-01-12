class Rectangle:
    def __init__(self,width=1,height=2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width*self.height
    def getPerimeter(self):
        return 2*(self.width+self.height)

def main():
    r1 = Rectangle(4,40)
    r2 = Rectangle(3.5,35.7)
    print("Rectangle 1")
    print("Width : {} Height : {} \nArea : {:.2f} Perimeter : {}".format(r1.width,r1.height,r1.getArea(),r1.getPerimeter()))
    print()
    print("Rectangle 2")
    print("Width : {} Height : {} \nArea : {:.2f} Perimeter : {}".format(r2.width,r2.height,r2.getArea(),r2.getPerimeter()))

main()
    