
def binaryToDecimal(binaryString):
    r = int(binaryString)
    n = 0
    i = 0
    d = 0
    while r !=0:
        n = r%10
        d = d+(n*(2**i))
        r = r//10 
        i +=1
    return d

def formatBinary(BinaryString):
    d = len(BinaryString)%4
    result = BinaryString
    for i in range(d):
        result = '0'+result
    return result 

def decimalToHex(decimal):
    decimal = int(decimal)
    if decimal <=9:
        return str(decimal)
    else:
        return chr(decimal+55)

def binaryToHex(binaryString): 
    binaryString = formatBinary(binaryString)
    n = 0
    m = 4
    result = ''
    while len(binaryString) >= m:
        decimal = binaryToDecimal(binaryString[n:m])
        deciToHex = decimalToHex(decimal)
        n = m
        m +=4
        result = result +deciToHex
    return result

def main():
    bi = input("Enter binary : ").strip()
    hex = binaryToHex(bi)
    print(f"Binary input : {bi}\nHexadecimal : {hex}")
main()