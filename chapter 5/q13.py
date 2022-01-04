count = 0
target = 10
for i in range(100,200):
    if (i%5==0 or i%6 ==0) and (i%30 !=0):
        print(f'{i} ',end=  '') 
        count +=1
    if count == target:
        print()
        target +=10
    