import math 
print('Degree \t Sin \t \t Cos ')
for i in range(0,361,10):
    theta = i*(math.pi/180)
    print('{} \t {:.4f} \t {:.4f} '.format(i,math.sin(theta),math.cos(theta)))