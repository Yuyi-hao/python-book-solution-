import time 
import random

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 10

startTime = time.time()


while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(1,15)
    number2 = random.randint(1,15)

    answer = eval(input("What is " + str(number1) + " + "+ str(number2) + "? "))

    if(answer == number1 + number2):
        print("You are correct !")
        correctCount +=1
    else:
        print('Your answer is wrong. \n {} + {} = {}'.format(number1,number2,number1+number2))
    count+=1

endtime = time.time()
testtime = int(endtime-startTime)
print('correct count is {} out of {} \n Test time is {}seconds '.format(correctCount,NUMBER_OF_QUESTIONS,testtime))