class QuardaticEquation():
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    # accessor 
    def geta(self):
        return self.__a 
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c
    def getDiscrimination(self):
        d = self.__b**2 - (4*self.__a*self.__c)
        return d 
    def getRoot1(self):
        if self.getDiscrimination() >= 0:
            root1 = (-self.__b + (self.getDiscrimination()**0.5))/(2*self.__a)
            return root1
        else:
            return 0
    def getRoot2(self):
        if self.getDiscrimination() >= 0:
            root2 = (-self.__b - (self.getDiscrimination()**0.5))/(2*self.__a)
            return root2
        else:
            return 0
def main():
    a = float(input("Enter the value of a : "))
    b = float(input("Enter the value of b : "))
    c = float(input("Enter the value of c : "))
    eq1 = QuardaticEquation(a,b,c)
    if eq1.getDiscrimination() < 0:
        print('The equation has no roots')
    elif eq1.getDiscrimination() ==0:
        print('One root is : {:.2f}'.format(eq1.getRoot1()))
    elif eq1.getDiscrimination() >0:
        print('Root 1 : {:.2f}\nRoot 2 : {:.2f}'.format(eq1.getRoot1(),eq1.getRoot2()))
    else:
        print('Error in class')

main()