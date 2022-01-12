import time
class Time:
    def __init__(self,time = int(time.time())):
        minute = time//60
        rsecond = time%60
        rminute = minute%60
        hour = minute//60
        currentHour = hour%24
        self.__hour = currentHour
        self.__minute = rminute
        self.__second = rsecond
    def getHour(self):
        return self.__hour
    def getMinute(self):
        return self.__minute
    def getsecond(self):
        return self.__second
    def setTime(self,elapseTime):
        minute = elapseTime//60
        rsecond = elapseTime%60
        rminute = minute%60
        hour = minute//60
        currentHour = hour%24
        self.__hour = currentHour
        self.__minute = rminute
        self.__second = rsecond

def main():
    time = Time()
    print('Current time is {}:{}:{}'.format(time.getHour(),time.getMinute(),time.getsecond()))
    e = int(input('Enter the elapsed time : '))
    time.setTime(e)
    print('The hour:minute:second for elapsed time is {}:{}:{}'.format(time.getHour(),time.getMinute(),time.getsecond()))

main()

