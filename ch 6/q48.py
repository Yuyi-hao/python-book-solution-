def format(number,width): 
    result = ''
    difference = width-len(str(number))
    if len(str(number)) > width or len(str(number)) == width:
        return int(str(number))
    else:
        while difference != 0:
            result += '0'
            difference -=1
    return result+str(number)
def main():
    n = int(input("Enter the number : "))
    width = int(input("Enter the width : "))
    newNumber = format(n,width)
    print(f'{newNumber}')
main()