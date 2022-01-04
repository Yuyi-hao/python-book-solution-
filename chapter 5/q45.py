d = int(input("Enter an integer: "))

hex = ""
value = d

while value != 0:
    h = value % 16
    if h >= 10:
        hex += chr(h + 55)
    else:
        hex += str(h)

    value //= 16

res = ""
print(hex)
for i in range(len(hex) - 1, -1, -1):
    res += hex[i]

print("The hexadecimal representation of", d, "is", res)