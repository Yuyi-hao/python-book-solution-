def isValid(n):
    if len(str(n))>=13 and len(str(n))<=16:
        return True
    return False 

def sumOfDoubleEvenPlace(n):
    length = len(str(n))
    r = n
    count = 1
    sumOfEvenDigits = 0
    for i in range(1,length+1,1):
        digit = r//(10**(length-i))
        r = n%(10**(length-i))
        if count%2 != 0:    
            evenDigit = digit*2
            if len(str(evenDigit)) >1:
                first = evenDigit%10 
                second = evenDigit//10
                evenDigit = first+second
            sumOfEvenDigits +=evenDigit

        count +=1
    return sumOfEvenDigits

def sumOfOddPlace(n):
    length = len(str(n))
    r = n
    count = 1
    sumOfOddDigits = 0
    for i in range(1,length+1,1):
        digit = r//(10**(length-i))
        r = n%(10**(length-i))
        if count%2 ==0:
            sumOfOddDigits +=digit
        count +=1
    return sumOfOddDigits


def correctDigit(n):
    if len(str(n))>=13 and len(str(n))<=16:
        return True
    return False 

def typeOfCard(n):
    length = len(str(n))
    # getting first digit
    firstDigit = n//(10**(length-1))
    firstTwoDigits = n//(10**(length-2))
    if correctDigit(n):
        if firstDigit == 4:
            return 'Visa cards'
        elif firstDigit == 5:
            return 'Mastercard credit cards'
        elif firstDigit == 6:
            return 'Discover cards'
        elif firstTwoDigits == 37:
            return 'American Express cards'
        else:
            return 'INVALID CARD NO.'
    else:
        return 'INVALID CARD NO.'
    

def main():
    n = int(input("Enter the credit card number : "))
    if isValid(n):
        if (sumOfDoubleEvenPlace(n)+sumOfOddPlace(n))%10 == 0:
            print('Card is valid and type of card is : ',end='')
            print(typeOfCard(n))
        else:
            print('Invalid card')
    else:
        print('Invalid card')

main()


