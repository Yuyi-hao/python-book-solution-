num = int(input("Enter an integer : "))

fiveAndSix = False 
fiveOrSix = False
both = True

if num%5==0 or num%6==0:
    fiveOrSix = True
    if num%5==0 and num%6==0:
        fiveAndSix = True
    if fiveOrSix and fiveAndSix:
        print('no')
        both = False
    
    print('Is {} divisible by 5 and 6? {} '.format(num,fiveAndSix))
    print('Is {} divisible by 5 or 6? {} '.format(num,fiveOrSix))
    print('Is {} divisible by 5 or 6, but not both? {}'.format(num,both)) 
else:
    fiveOrSix = False
    fiveOrSix = False
    print("{} is neither divisible be 5 nor 6 ".format(num))


