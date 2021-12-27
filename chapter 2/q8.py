# Science: calculate energy

amountOfWater = eval(input("Enter the amount od water in kilograms : "))
initialTemp = eval(input("Enter the initial temperature : "))
finalTemp = eval(input("Enter the final temperature : "))

energy = amountOfWater*( finalTemp - initialTemp)*4184
print('The energy needed is {:.3f}'.format(energy))