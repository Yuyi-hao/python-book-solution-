


def decimalToBinary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal%2) + binary
        decimal = decimal//2
    return binary


def main():
    decimal = int(input("Enter binary : "))
    binary = decimalToBinary(decimal)
    print(f"Decimal input : {decimal}\nBinary : {binary}")
main()