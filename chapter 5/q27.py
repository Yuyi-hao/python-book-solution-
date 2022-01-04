j = 0
k = 0
l = 0
for i in range(1,10000,1):
    j += ((-1)**(i+1))/(2*i-1) 
for i in range(1,20000,1):
    k += ((-1)**(i+1))/(2*i-1)
for i in range(1,100000,1):
    l += ((-1)**(i+1))/(2*i-1)

pi1 = 4*j
pi2 = 4*k
pi3 = 4*l
print(pi1, pi2, pi3)