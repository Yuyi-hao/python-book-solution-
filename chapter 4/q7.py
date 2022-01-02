# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100
 
# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount


dollar = ''
quaters = ''
dimes = ''
nickels =''
pennies = ''

if numberOfOneDollars> 0:
    if numberOfOneDollars > 1:
        dollar = '{} dollars'.format(numberOfOneDollars)
    else:
        dollar = '{} dollar'.format(numberOfOneDollars)
if numberOfQuarters> 0:
    if numberOfQuarters > 1:
        quaters = '{} quaters'.format(numberOfQuarters)
    else:
        quaters = '{} quater'.format(numberOfQuarters)
if numberOfDimes> 0:
    if numberOfDimes > 1:
        dimes = '{} dimeses'.format(numberOfDimes)
    else:
        dimes = '{} dimes'.format(numberOfDimes)
if numberOfNickels> 0:
    if numberOfNickels > 1:
        nickels = '{} nickels'.format(numberOfNickels)
    else:
        nickels = '{} nickel'.format(numberOfNickels)
if numberOfPennies> 0:
    if numberOfPennies > 1:
        nickels = '{} nickels'.format(numberOfPennies)
    else:
        nickels = '{} nickel'.format(numberOfPennies)


# Display the results
print("Your amount", amount, "consists of\n", 
    "\t", dollar, "\n", 
    "\t", quaters, "\n",
    "\t", dimes,  "\n",
    "\t", nickels, "\n",
    "\t", pennies, "")
