class Complex:
    def __init__(self,a=0,b=0):
        self.__a = a
        self.__b = b
    def getRealPart(self):
        return self.__a
    def getImaginaryPart(self):
        return self.__b
    def __add__(self,c1):
        a = self.__a+c1.getRealPart()
        b = self.__b+c1.getImaginaryPart()
        return f'({self.__a} + {self.__b}i) + ({c1.getRealPart()} + {c1.getImaginaryPart()}i) = ({a} + {b}i)'

    def __sub__(self,c1):
        a = self.__a-c1.getRealPart()
        b = self.__b-c1.getImaginaryPart()
        return f'({self.__a} + {self.__b}i) - ({c1.getRealPart()} + {c1.getImaginaryPart()}i) = ({a} + {b}i)'
        
    def __mul__(self,c1):
        a = self.__a*c1.getRealPart() - self.__b*c1.getImaginaryPart()
        b = self.__b*c1.getRealPart() + self.__a*c1.getImaginaryPart()
        return f'({self.__a} + {self.__b}i) * ({c1.getRealPart()} + {c1.getImaginaryPart()}i) = ({a} + {b}i)'

    def __truediv__(self,c1):
        d = (c1.getRealPart()**2 + c1.getImaginaryPart()**2)
        a = (self.__a*c1.getRealPart() + self.__b*c1.getImaginaryPart())/d
        b = (self.__b*c1.getRealPart() - self.__a*c1.getImaginaryPart())/d
        return f'({self.__a} + {self.__b}i) / ({c1.getRealPart()} + {c1.getImaginaryPart()}i) = ({a} + {b}i)'

    def __abs__(self):
        abs = ((self.__a*self.__a)+(self.__b*self.__b))**0.5
        return f'|({self.__a} + {self.__b}i)| = {abs}'
    def __str__(self):
        return f'({self.__a}+{self.__b}i)'
    
    
def main():
    a,b = eval(input("Enter the first complex number : "))
    c,d = eval(input("Enter the second complex number : "))
    c1 = Complex(a,b)
    c2 = Complex(c,d)
    print(c1.__add__(c2))
    print(c1.__sub__(c2))
    print(c1.__mul__(c2))
    print(c1.__truediv__(c2))
    print(c1.__abs__())
main()