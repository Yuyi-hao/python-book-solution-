def digit(isbn):
    isbn = str(isbn)
    length = len(isbn)
    result = 0
    r = ''
    for i in range(0,length,2):
        result += int(isbn[i])
    for i in range(1,length,2):
        result += 3*int(isbn[i])
    r = 10-result%10
    if r == 10:
        digit13 = '0'
    else:
        digit13 = str(r)
    return digit13

def main():
    isbn = input("Enter the first 12 digit of an ISBN-13 as a string : ")
    result = isbn + str(digit(isbn))
    print(f"The ISBN-13 number is {result}")
main()