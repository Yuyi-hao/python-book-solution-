def tenthDigit(isbn):
    d = str(isbn)
    j = 1
    r = 0
    d10 = 1
    for i in d:
        r += j*int(i)
        j +=1
    if  r%11==10:
        d10 = 'X'
    return str(d10)

def main():
    isbn = input('Enter the first 9 digits an ISBN-10 as a string : ')
    isbn2 = isbn + tenthDigit(isbn)
    print(f'The ISBN-10 NUMBER IS {isbn2}')

main()