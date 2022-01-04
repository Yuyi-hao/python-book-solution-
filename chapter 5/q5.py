POUNDS_PER_KILOGRAM = 2.2
KILOGRAM_PER_POUND = 0.45
print('Kilograms \t Pounds \t | \t Pounds \t Kilograns')
for i in range(1,200,2):
    a = 2.5*i+17.5
    print('{} \t \t {:.1f} \t | \t {:.0f} \t \t {:.2f}'.format(i,i*POUNDS_PER_KILOGRAM,(a),(a*KILOGRAM_PER_POUND)))