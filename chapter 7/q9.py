class LinearEquation():
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # accessor 
    def geta(self):
        return self.__a 
    def getb(self):
        return self.__b
    def getc(self):
        return self.__c 
    def getd(self):
        return self.__d 
    def gete(self):
        return self.__e
    def getf(self):
        return self.__f
    
    def isSolvable(self):
        d = self.__a * self.__d - self.__b * self.__c
        if d == 0:
            return False
        else:
            return True 
    
    def getX(self):
        if self.isSolvable():
            d = (self.__a*self.__d)-(self.__b*self.__c)
            n = (self.__e*self.__d)-(self.__b*self.__f)
            x = n/d
            return x 
        else:
            return 0 
    def getY(self):
        if self.isSolvable():
            d = (self.__a*self.__d)-(self.__b*self.__c)
            n = (self.__a*self.__f)-(self.__e*self.__c)
            y = n/d
            return y 
        else:
            return 0

def main():
    x1,y1 = eval(input("Enter starting point of line 1 :"))
    x2,y2 = eval(input("Enter ending point of line 1 :"))
    x3,y3 = eval(input("Enter starting point of line 2 :"))
    x4,y4 = eval(input("Enter ending point of line 2 :"))
    a = y1 - y2
    b = -x1 + x2
    c = y3 - y4
    d = -x3 + x4
    e = -y1 * (x1 - x2) + (y1 - y2) * x1
    f = -y3 * (x3 - x4) + (y3 - y4) * x3
    pair = LinearEquation(a,b,c,d,e,f)
    if pair.isSolvable():
        print('X : {:.2f} and Y : {:.2f}'.format(pair.getX(),pair.getY()))
    else:
        print('The equation has no solution')
main()
