n1 = int(input("Enter the first integer : "))
n2 = int(input("Enter the second integer : "))
d = min(n1,n2)

while d >=2:
    if n1%d == 0 and n2%d == 0:
        break
    d = d-1

print(d)