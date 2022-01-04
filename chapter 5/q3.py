POUNDS_PER_KILOGRAM = 2.2
print('Kilograms \t Pounds')
for i in range(1,200,2):
    print('{} \t \t {:.1f}'.format(i,i*POUNDS_PER_KILOGRAM))