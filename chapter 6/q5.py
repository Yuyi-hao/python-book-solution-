def displaySortedNumbers(n1,n2,n3):
    sum = n1+n2+n3 
    maxN = max(n1,n2,n3)
    minN = min(n1,n2,n3)
    middle = sum-(maxN+minN)
    print(minN,middle,maxN)
def main():
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number  : "))
    num3 = float(input("Enter third number  : "))
    displaySortedNumbers(num1,num2,num3)
main()