import random 
n1 = random.randint(0,9)
n2 = random.randint(0,9)

while n1 == n2:
    n2 = random.randint(0,9)

userInput = int(input("Enter two digit lottery number : "))
firstDigit = userInput//10
secondDigit = userInput%10 

if userInput == int(str(n1)+str(n2)):
    print("Exact match : you won $10,000")
elif (secondDigit == n1) and (firstDigit == n2):
    print("Match all digits : you won $3,000")
elif firstDigit == n1 or secondDigit == n2 or firstDigit == n2 or secondDigit == n1:
    print("Match one digit : you won $1,000 ")
else:
    print("Sorry, no match") 