class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getStockName(self):
        return self.__name
    def getStockSymbol(self):
        return self.__symbol
    def getPreviousPrice(self):
        return self.__previousClosingPrice
    def setPreviousPrice(self,price):
        self.__previousClosingPrice = price
        return self.__previousClosingPrice
    def getCurrentPrice(self):
        return self.__currentPrice
    def setCurrentPrice(self,newprice):
        self.__currentPrice = newprice
    def getChangepercent(self):
        return ((self.__currentPrice - self.__previousClosingPrice)/self.__previousClosingPrice)*100
def main():
    s1 = Stock('INCT','intel',20.5,20.35)
    print(s1.getChangepercent())
main()