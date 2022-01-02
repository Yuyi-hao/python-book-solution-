import turtle
x,y = eval(input("Enter the point(x,y) : "))
width = 100
height = 50
dx = abs(0-x)
dy = abs(0-y)
turtle.penup()
turtle.goto((-width/2),(-height/2))
turtle.pendown()
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.dot(6,'red')
turtle.penup()
turtle.goto(x-100,y-15)



if dx<(width/2) and y<(height/2):
    position = 'inside'
else:
    position = 'outside'
turtle.write('The point is {} rectangle'.format(position))
print('The point is {} rectangle'.format(position))

turtle.done()


