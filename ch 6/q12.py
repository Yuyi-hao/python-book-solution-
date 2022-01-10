def printChars(ch1,ch2,numberPerLine):
    ascii1 = ord(ch1)
    ascii2 = ord(ch2)
    target = numberPerLine
    count = 0
    for i in range(ascii1,ascii2+1,1):
        print(chr(i),end= ' ')
        count +=1
        if count == target:
            print()
            target += numberPerLine
        
def main():
    ch1 = input('Enter the starting character : ')
    ch2 = input('Enter the ending character : ')
    numberPerLine = int(input("Enter the character per line : "))
    printChars(ch1,ch2,numberPerLine)
main()
