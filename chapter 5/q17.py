count = 1
for i in range(33,127):
    print(chr(i), end= ' ')
    count +=1
    if count%10 == 0:
        print() 