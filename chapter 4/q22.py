x,y = eval(input("Enter the point(x,y) : "))

d = ((x**2)+(y**2))**0.5

if d>10:
    position = 'outside'
else:
    position = 'inside'
print('The point is {} circle'.format(position))


