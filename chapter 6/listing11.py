from random import randint
# get random charater between ch1 and ch2 
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1),ord(ch2)))

# get a random lower case letter 
def getRandomLowerCaseLetter():
    return getRandomCharacter('a','z')
# get a random upper case letter  
def getRandomUpperCaseLetter():
    return getRandomCharacter('A','Z')

# genrate a random single digit 
def getRandomDigitCharater():
    return getRandomCharacter('0','9')
# get random character
def getRandomASCIICharacter():
    return chr(randint(0,127))