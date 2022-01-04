INTIAL_AMOUNT = 10000
RATE = 0.05
newPrice = INTIAL_AMOUNT
for i in range(1,11,1):
    tution = newPrice*RATE
    newPrice = tution+newPrice 
print('The tution in ten years is {:.2f}'.format(newPrice))
print('The tution in four years is {:.2f}'.format(4*newPrice))


