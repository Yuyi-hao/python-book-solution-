# Physics:  find  runway  length

speed,acceration = eval(input("Enter speed and acceleration (speed,acceleration) : "))

length = (speed**2)/(2*acceration)

print('The minimum runway length for this airplane is {:.3f}'.format(length))