sumLtoR = 0 
sumRtoL = 0
for i in range (1,50001,1):
    sumLtoR += 1/i

print(sumLtoR)

for j in range(50000,0,-1):
    sumRtoL += 1/i

print(sumRtoL)

