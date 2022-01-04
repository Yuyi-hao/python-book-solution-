MILES_PER_KILOMETER = 1.609
print('Miles \t  \t Kilometers')
for i in range(1,11,1):
    print('{} \t \t {:.3-+f}'.format(i,i*MILES_PER_KILOMETER))