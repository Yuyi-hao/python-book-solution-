import random

a,b,c = random.randint(0,9),random.randint(0,9),random.randint(0,9)


lotteryNum = int(f'{a}'+f'{b}'+f'{c}') # shortcut for formatted string and converting them into num 
print(lotteryNum)
guess = int(input("Enter your guess : "))

thirdDigit =  guess%10
secondDigit = (guess//10)%10
firstDigit  = guess//100

print(firstDigit,secondDigit,thirdDigit)

if guess == lotteryNum:
    print("You won price worth of $10,000 ")
elif (firstDigit == b or firstDigit == c) and (secondDigit == c or secondDigit == a) :
    print("You won the price worth of $3,000")
elif firstDigit == b or firstDigit == c or secondDigit == c or secondDigit == a or firstDigit == a or secondDigit == b or thirdDigit == c:
    print("You won the price worth of $1,000")
else:
    print("You lose 😢!!")
