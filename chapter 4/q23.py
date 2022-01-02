x,y = eval(input("Enter the point(x,y) : "))

dx = abs(0-x)
dy = abs(0-y)

if dx<(10/2) and y<(5/2):
    position = 'inside'
else:
    position = 'outside'
print('The point is {} rectangle'.format(position))
