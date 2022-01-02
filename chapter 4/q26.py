num = int(input("Enter a three-digit integer : "))
thirdDigit =  num%10
secondDigit = (num//10)%10
firstDigit  = num//100
reverse = int(f'{thirdDigit}'+f'{secondDigit}'+f'{firstDigit}')
if num == reverse:
    print("{} is a palindrome".format(num))
else:
    print("{} is not a palindrome".format(num))
