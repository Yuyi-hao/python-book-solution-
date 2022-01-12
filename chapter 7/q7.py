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
        d = (self.__a*self.__d)-(self.__b*self.__c)
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
            d = self.__a*self.__d-self.__b*self.__c
            n = self.__a*self.__f-self.__e*self.__c
            y = n/d
            return y 
        else:
            return 0


def main():
    a = float(input("Enter the value of a : "))
    b = float(input("Enter the value of b : "))
    c = float(input("Enter the value of c : "))
    d = float(input("Enter the value of d : "))
    e = float(input("Enter the value of e : "))
    f = float(input("Enter the value of f : "))
    pair = LinearEquation(a,b,c,d,e,f)
    if pair.isSolvable():
        print('X : {:.2f} and Y : {:.2f}'.format(pair.getX(),pair.getY()))
    else:
        print('The equation has no solution')
main()
