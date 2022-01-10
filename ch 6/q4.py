def reverse(number):
    length = len(str(number))
    returnString = ''
    for i in range(1,length+1,1):
        digit = number%10
        returnString +=str(digit)
        number = number//10
    return int(returnString)


def main():
    num = int(input("Enter the number : "))
    print("{} reverse {}".format(num,reverse(num)))

main()
