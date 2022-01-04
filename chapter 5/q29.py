YEAR_PER_LINE = 10
target = YEAR_PER_LINE
count = 0
for i  in range(2001,2100,1):
    if i%100 != 0 and i%4 == 0:
        print(i,end=' ')
        count +=1
    if count == target:
        target +=YEAR_PER_LINE
        print()

