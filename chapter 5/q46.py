 print("Enter ten numbers : ",end='') 
sum = 0
n = 10
sum2 = 0
for i in range(1,n+1,1):
    num = float(input())
    sum += num
    sum2 += num**2
average = sum/(i)
deviation = ((sum2-sum*sum/i)/(i-1))**0.5
print('The mean is {:.2f}'.format(average))
print('The standard deviation is {:.5f}'.format(deviation))