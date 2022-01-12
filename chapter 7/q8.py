import time
class StopWatch:
    def __init__(Self):
        Self.__startTime = time.time()
        Self.__endTime = 0
    def start(Self):
        Self.__startTime = time.time()
        return Self.__startTime
    def stop(Self):
        Self.__endTime = time.time()
        return Self.__endTime
    def getElapsedTime(Self):
        t = Self.__endTime - Self.__startTime
        return t*1000 
def main():
    sum = 0
    t1 = StopWatch()
    t1.start()
    for i in range(1000000):
        sum +=i
    print(f'Total : {sum}') 
    t1.stop()
    print('Total time taken : {}milliseconds'.format(t1.getElapsedTime()))
main()

