def sumDigits(n):
    length = len(str(n))
    sum = 0
    for i in range(1,length+1,1):
        digit = n%10
        sum +=digit
        n = n//10
    return sum 
def main():
    num = int(input("Enter your number : "))
    sum = sumDigits(num)
    print(sum)
main()