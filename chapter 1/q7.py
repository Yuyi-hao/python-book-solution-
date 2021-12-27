n = 6 
sum = 0
sign = -1
for i in range(1,n*2,2):
    sign = sign*(-1)
    
    i = i*sign
    
    sum = sum + 1/i
    
print("{:.2f}".format(sum*4))



        