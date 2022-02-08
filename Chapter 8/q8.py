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

def main():
    bi = input("Enter binary : ").strip()
    decimal = binaryToDecimal(bi)
    print(f"Binary input : {bi}\nDecimal : {decimal}")
main()