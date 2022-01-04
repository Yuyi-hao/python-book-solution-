n = 1
m = 7 
count = 0
for i in range(n,m+1,1):
    for j in range(i+1,m+1,1):
        print(i,j)
        count +=1
print('The total number of all combinations is {}'.format(count))