class Fan():
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,speed=SLOW,on=False,radius=5,color='blue'):
        self.__speed = speed
        self.__on = on 
        self.__radius = radius
        self.__color = color
    
    #accessor 
    def getSpeed(self):
        return self.__speed
    def getOn(self):
        return self.__on
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    # mutator
    def setSpeed(self,newspeeed):
        self.__speed = newspeeed
        return self.__speed
    def setOn(self,state):
        self.__on = state
        return self.__on
    def setColor(self,newcolor):
        self.__color = newcolor
        return self.__color
    def setRadius(self,newRadius):
        self.__radius = newRadius
        return self.__radius

def main():
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    fan1 = Fan(FAST,True,10,'Yellow')
    fan2 = Fan(MEDIUM,False,5,'blue')
    print('Fan 1')
    print('Fan speed : {}\nFan radius : {}\nFan color : {}\nFan on : {}'.format(fan1.getSpeed(),fan1.getRadius(),fan1.getColor(),fan1.getOn()))
    print('Fan 2')
    print('Fan speed : {}\nFan radius : {}\nFan color : {}\nFan on : {}'.format(fan2.getSpeed(),fan2.getRadius(),fan2.getColor(),fan2.getOn()))
main()
    