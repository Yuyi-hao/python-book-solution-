def getNumber(upperCaseLetter):
    upperCaseLetter = str(upperCaseLetter)
    result = ''
    for i in upperCaseLetter:
        if i.isalpha():
            if i == 'A' or i == 'B' or i == 'C':
                result +='2'
            elif i =='D' or i=='E' or i=='F':
                result +='3'
            elif i =='G' or i=='H' or i=='I':
                result +='4'
            elif i =='J' or i=='K' or i=='L':
                result +='5'
            elif i =='M' or i=='N' or i=='O':
                result +='6'
            elif i =='P' or i=='Q' or i=='R' or i=='S':
                result +='7'
            elif i =='T' or i=='U' or i=='V':
                result +='8'
            elif i =='W' or i=='X' or i=='Y' or i=='Z':
                result +='9'
        else:
            result += i
    return result

def main():
    string = input("Enter a string : ").upper().strip()
    print(getNumber(string))
main()