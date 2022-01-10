def reverse(number):
    length = len(str(number))
    returnString = ''
    for i in range(1,length+1,1):
        digit = number%10
        returnString +=str(digit)
        number = number//10
    return int(returnString)

def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

def main():
    num = int(input("Enter the number : "))
    if isPalindrome(num):
        print("The number is a palindrome")
    else:
        print("The number isn't a palindrome")

main()
