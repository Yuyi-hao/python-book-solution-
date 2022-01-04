MILES_PER_KILOMETER= 0.621
KILOMETER_PER_MILE = 1.609
print('Kilograms \t Pounds  | Pounds \t Kilograns')
for i in range(1,11,1):
    a = i*5+15
    print('{} \t \t {:.1f} \t | {:.0f} \t \t {:.2f}'.format(i,i*KILOMETER_PER_MILE,(a),(a*MILES_PER_KILOMETER)))